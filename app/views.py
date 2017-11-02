""" App views file"""
from werkzeug.utils import secure_filename

from app import app, render_template, redirect, request, url_for, os
from flask import session

from app.models.Users import Users
from app.models.Category import Category
from app.models.Recipe import Recipe

USER = Users()
CATEGORY = Category()
RECIPE = Recipe()


@app.route('/')
def home():
    """Landing page"""
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login page"""
    if 'is_logged_in' in session.keys():
        return redirect(url_for('home'))
    response = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        response = USER.login_user(email, password)
        if response['status'] == 'success':
            session['is_logged_in'] = {
                "username": response['user']['username'],
                "email": response['user']['email'],
                "password": response['user']['password'],
                "id": response['user']['id']
            }
            return redirect(url_for('home'))

    return render_template('login.html', data=response)


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Register page"""
    if 'is_logged_in' in session.keys():
        return redirect(url_for('home'))
    response = None
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_again = request.form['password-again']

        response = USER.register_user(username, email, password, password_again)

        if response['status'] == "success":
            return render_template('login.html', data=response, msg=response['message'])

    return render_template("register.html", data=response)


@app.route('/logout', methods=['GET'])
def logout():
    """Logout page"""
    if 'is_logged_in' in session.keys():
        session.pop('is_logged_in', None)
    return redirect(url_for('login'))


@app.route('/categories', methods=['GET'])
def get_categories():
    """Get categories"""
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    user_id = session['is_logged_in']['id']
    response = CATEGORY.all_categories(user_id) or None
    return render_template('allcategories.html', data=response)


@app.route('/addcategory', methods=['GET', 'POST'])
def add_category():
    """Add category"""
    response = None
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        user_id = session['is_logged_in']['id']
        image = request.files['file']
        response = CATEGORY.create_category(name, description, user_id, image)
        if response['status'] == 'success':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('get_categories'))
    return render_template('addcat.html', data=response)


@app.route('/categories/<category_id>', methods=['GET'])
def get_category(category_id):
    """Get single category"""
    response = CATEGORY.single_category(category_id)
    return render_template('singlecategory.html', data=response)


@app.route('/delcategory/<category_id>', methods=['GET'])
def del_category(category_id):
    """Delete category"""
    CATEGORY.delete_category(category_id)
    return redirect(url_for('get_categories'))


@app.route('/updatecategory/<_id>', methods=['GET', 'POST'])
def update_category(_id):
    """Update category"""
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    response = CATEGORY.single_category(_id)
    if request.method == "POST":
        category_id = _id
        name = request.form['name']
        description = request.form['description']
        user_id = session['is_logged_in']['id']
        image = ''
        if request.files['file']:
            image = request.files['file']

        response = CATEGORY.update_category(category_id, name, description, user_id, image)
        if response['status'] == 'success':
            if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('get_categories'))

    return render_template('updatecategory.html', data=response)


@app.route('/category/<_id>/addrecipe', methods=['POST', 'GET'])
def addrecipe(_id):
    """Add recipe"""
    response = None
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        ingredients = request.form['ingredients']
        direction = request.form['direction']
        category_id = _id
        user_id = session['is_logged_in']['id']
        image = request.files['file']

        response = RECIPE.create_recipe(name, time, ingredients, direction,
                                        category_id, user_id, image)
        if response['status'] == 'success':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('recipes', _id=_id))

    return render_template('addrecipe.html', data=response)


@app.route('/category/<_id>/recipes', methods=['GET'])
def recipes(_id):
    """Available recipes"""
    category_id = _id
    if not CATEGORY.check_if_exists(category_id):
        return redirect(url_for('add_category'))
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    user_id = session['is_logged_in']['id']
    response = RECIPE.view_recipes(user_id, category_id)

    return render_template('recipes.html', data={
        "category_id": category_id,
        "response": response})


@app.route('/category/<_id>/delrecipe/<recipe_id>', methods=['GET'])
def del_recipe(_id, recipe_id):
    """Delete recipe"""
    RECIPE.delete_recipe(recipe_id)
    return redirect(url_for('recipes', _id=_id))


@app.route('/category/<_id>/updaterecipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(_id, recipe_id):
    """Update recipe"""
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    response = RECIPE.single_recipe(recipe_id)
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        ingredients = request.form['ingredients']
        direction = request.form['direction']
        category_id = _id
        user_id = session['is_logged_in']['id']
        image = ''
        if request.files['file']:
            image = request.files['file']

        response = RECIPE.update_recipe(recipe_id, name, time, ingredients,
                                        direction, category_id, user_id, image)
        if response['status'] == 'success':
            if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('recipes', _id=category_id))

    return render_template('updaterecipe.html', data=response)
