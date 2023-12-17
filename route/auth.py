import os
import flask as fk
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required, logout_user
from app.models.User import  User
from extensions import db


auth_blueprint = fk.Blueprint('auth', os.getenv("APP_NAME"),template_folder='./resources/view',static_folder='./public')

@auth_blueprint.route('/login')
def login():
    fk.session.pop('_flashes', None)
    return fk.stream_template('frontend/login.html')

@auth_blueprint.route('/signup')
def signup():
    fk.session.pop('_flashes', None)
    return fk.stream_template('frontend/signup.html')


@auth_blueprint.route('/login', methods=['POST'])
def login_post():
    email = fk.request.form.get('email').lower()
    password = fk.request.form.get('password')
    remember = True if fk.request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        fk.flash('Please check your login details and try again.')
        return fk.stream_template('frontend/login.html')

    login_user(user,remember=remember)
    return fk.redirect(fk.url_for('web.index'))

@auth_blueprint.route('/signup', methods=['POST'])
def signup_post():
    email = fk.request.form.get('email').lower()
    name = fk.request.form.get('name')
    password = fk.request.form.get('password')

    user = User.query.filter_by(email=email).first() 

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        fk.flash('this email address is already registered at our database.')
        return fk.stream_template('frontend/signup.html')

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return fk.redirect(fk.url_for('auth.login'))
    

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return fk.redirect(fk.url_for('web.index'))