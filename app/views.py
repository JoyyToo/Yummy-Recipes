from app import app, render_template, redirect, request, url_for, jsonify, session
from flask import flash
from app.models.Users import Users

user = Users()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        response = user.login_user(email, password)
        print(response)
        if response['status'] == 'success':
            session['is_logged_in'] = {
                "email": response['user']['email'],
                "password": response['user']['password'],
                "id": response['user']['id']
            }
            return redirect(url_for('home'))

    return render_template('login.html', data=response)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_again = request.form['password-again']

        response = user.register_user(username, email, password, password_again)

        print(response)
        return redirect(url_for('login'))

    return render_template("register.html")


@app.route('/logout', methods=['GET'])
def logout():
    if 'is_logged_in' in session.keys():
        del session['is_logged_in']
        return redirect(url_for('home'))
    return redirect(url_for('register'))
