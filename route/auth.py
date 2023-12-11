import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from app.models.User import  User


auth = Blueprint('auth', os.getenv("APP_NAME"),template_folder='./resources/view',static_folder='./public')

@auth.route('/login')
def login():
    return render_template('frontend/login.html')

@auth.route('/signup')
def signup():
    return render_template('frontend/signup.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) 

    return redirect(url_for('main.profile'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

@auth.route('/logout')
def logout():
    return 'Logout'