from flask import Flask, session, render_template, redirect, url_for, request, flash, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user
from datetime import date, datetime
import jwt
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123samsamsam@localhost:5432/assignment3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisissekreto'

from models import *


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['GET'])
def index2():
    return render_template('index2.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(first_name=request.form['first_name'], last_name=request.form['last_name'], gender=request.form['gender'], email=request.form['email'], password=request.form['password'])
        print('signup')
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index2'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       user = User.query.filter_by(username=username, password=password).first()

       if not user:
           error = 'Invalid username or password!'
       else:
           login_user(user)
           flash('You were successfully logged in')
           return redirect(url_for('index'))

    return render_template('login.html', error=error)



@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('profile.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


# @app.route('/create')
# def create():
#     return render_template('after_register.html')


# @app.route('/create_list')
# def create_list():
#     return render_template('create_list.html')