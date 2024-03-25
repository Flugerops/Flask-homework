from .. import app
from flask import render_template, url_for, redirect, request


users = {}


@app.route('/')
def index():
    return render_template('base.html')


@app.get('/auth')
def auth_get():
    return render_template('auth.html')


@app.post('/auth')
def auth_post():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]['password'] == password:
        return render_template('welcome.html', username=username)
    else:
        return render_template('auth.html', message="Неправильний username або пароль!")

@app.get('/register')
def register_get():
    return render_template('register.html')

@app.post('/register')
def register_post():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        return render_template('register.html', message="Користувач з таким username вже існує!")
    else:
        users[username] = {'password': password}
        print(users)
        return render_template('welcome.html', username=username)
