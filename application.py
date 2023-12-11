import os
from flask import Flask,Blueprint,request,url_for,render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import Column, Integer
from core.route.route_helper import route_function_wrapper
from route.web import web_blueprint 
from route.api import api_blueprint
from route.auth import auth
from app.models.User import  User 

from extensions import (
    bcrypt,
    db,
    login_manager
)

def register_extensions(app):
    ###---------------------------------
    ### Register Flask extensions.
    ###---------------------------------
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    return None


def register_blueprints(app):
    ###---------------------------------
    ### Register Flask blueprints.
    ###---------------------------------
    app.register_blueprint(web_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(auth)
    return None

def create_app():
    load_dotenv()
    ###-----------------------------------------------------------------------------------------------------------
    ### make the app, set name from .env file | change the template and staic folder path to our current structure
    ###-----------------------------------------------------------------------------------------------------------
    app = Flask(os.getenv("APP_NAME"),template_folder='./resources/view',static_folder='./public')

    ###-----------------------------------------------------------------------------------------------------------------------
    ### set the MySQl configs , make the abstract class of BaseModel with one engin therefore other models can inherit form it 
    ###-----------------------------------------------------------------------------------------------------------------------
    mysql_user = os.getenv('DB_USER')
    mysql_password = os.getenv('DB_PASS')
    mysql_host = os.getenv('DB_HOST')
    mysql_db = os.getenv('DB_NAME')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{mysql_user}:{mysql_password}@{mysql_host}:5432/{mysql_db}'
    ###---------------------------------
    ### bind app to extensions and blueprints
    ###---------------------------------
    register_extensions(app)
    register_blueprints(app)
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


###---------------------------------
### run Application
###---------------------------------
if __name__ == '__main__':
    application = create_app()
    with application.app_context():
        db.create_all()
    application.run(host='0.0.0.0', port=5000,debug=True)