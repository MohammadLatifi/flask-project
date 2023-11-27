from flask import Blueprint
from core.route.route_helper import route_function_wrapper
from app.controllers.HomeController import HomeController
web_blueprint = Blueprint('web', __name__)

###---------------------------------
### Web routes defenitions goes here
###
###---------------------------------

@web_blueprint.route('/')
def home():
    return route_function_wrapper(HomeController(),'home')()

@web_blueprint.route('/about')
def about():
    return route_function_wrapper(HomeController(),'about')()
