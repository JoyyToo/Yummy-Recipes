from werkzeug.utils import secure_filename

from app import app, render_template, redirect, request, url_for, jsonify, os
from flask import session
from app.models.Users import Users
from app.models.Category import Category
from app.models.Recipe import Recipe

user = Users()
cat = Category()
rec = Recipe()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'is_logged_in' in session.keys():
        return redirect(url_for('home'))
    response = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        response = user.login_user(email, password)
        if response['status'] == 'success':
            session['is_logged_in'] = {
                "username": response['user']['username'],
                "email": response['user']['email'],
                "password": response['user']['password'],
                "id": response['user']['id']
            }
            return redirect(url_for('get_categories'))

    return render_template('login.html', data=response)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if 'is_logged_in' in session.keys():
        return redirect(url_for('home'))
    response = None
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_again = request.form['password-again']

        response = user.register_user(username, email, password, password_again)

        if response['status'] == "success":
            return redirect(url_for('login'))

    return render_template("register.html", data=response)


@app.route('/logout', methods=['GET'])
def logout():
    if 'is_logged_in' in session.keys():
        session.pop('is_logged_in', None)
    return redirect(url_for('login'))


@app.route('/categories', methods=['GET'])
@app.route('/categories/', methods=['GET'])
def get_categories():
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    user_id = session['is_logged_in']['id']
    response = cat.all_categories(user_id) if cat.all_categories(user_id) else None
    return render_template('allcategories.html', data=response)


@app.route('/addcategory', methods=['GET', 'POST'])
def add_category():
    response = None
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        user_id = session['is_logged_in']['id']
        image = request.files['file']
        response = cat.create_category(name, description, user_id, image)
        if response['status'] == 'success':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('get_categories'))
    return render_template('addcat.html', data=response)


@app.route('/categories/<cat_id>', methods=['GET'])
def get_category(cat_id):
    response = cat.single_category(cat_id)
    return render_template('singlecategory.html', data=response)


@app.route('/delcategory/<cat_id>', methods=['GET'])
def del_category(cat_id):
    response = cat.delete_category(cat_id) if cat.delete_category(cat_id) else None
    return redirect(url_for('get_categories'))


@app.route('/updatecategory/<_id>', methods=['GET', 'POST'])
def update_category(_id):
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    response = cat.single_category(_id)
    if request.method == "POST":
        cat_id = _id
        name = request.form['name']
        description = request.form['description']
        user_id = session['is_logged_in']['id']
        image = ''
        if request.files['file']:
            image = request.files['file']

        response = cat.update_category(cat_id, name, description, user_id, image)
        if response['status'] == 'success':
            if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('get_categories'))

    return render_template('updatecategory.html', data=response)


@app.route('/category/<_id>/addrecipe', methods=['POST', 'GET'])
def addrecipe(_id):
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

        response = rec.create_recipe(name, time, ingredients, direction, category_id, user_id, image)
        if response['status'] == 'success':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('recipes', _id=_id))

    return render_template('addrecipe.html', data=response)


@app.route('/category/<_id>/recipes', methods=['GET'])
def recipes(_id):
    cat_id = _id
    if not cat.check_if_exists(cat_id):
        return redirect(url_for('add_category'))
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    user_id = session['is_logged_in']['id']
    response = rec.view_recipes(user_id)

    return render_template('recipes.html', data={
        "cat_id": cat_id,
        "response": response})


@app.route('/category/<_id>/delrecipe/<recipe_id>', methods=['GET'])
def del_recipe(_id, recipe_id):
    response = rec.delete_recipe(recipe_id) if rec.delete_recipe(recipe_id) else None
    return redirect(url_for('recipes', _id=_id))


@app.route('/category/<_id>/updaterecipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(_id, recipe_id):
    if 'is_logged_in' not in session.keys():
        return redirect(url_for('login'))
    response = rec.single_recipe(recipe_id)
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

        response = rec.update_recipe(recipe_id, name, time, ingredients, direction, category_id, user_id, image)
        if response['status'] == 'success':
            if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('recipes', _id=category_id))

    return render_template('updaterecipe.html', data=response)