from flask import Flask
from dotenv import load_dotenv
import os
from route.web import web_blueprint
from route.api import api_blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
###-------------------
### Load the .env file
###-------------------

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

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'

db = SQLAlchemy(app)

class BaseModel(db.Model):
    __abstract__ = True
    

###---------------------------------
### include the web and api routes
###---------------------------------
app.register_blueprint(web_blueprint)
app.register_blueprint(api_blueprint)

app.run(debug=True)