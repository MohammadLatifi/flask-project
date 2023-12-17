import os
import flask as fk
from flask_login import login_required, current_user
from core.route.route_helper import route_function_wrapper
from app.controllers.HomeController import HomeController
from app.models.TechTalent import TechTalent
web_blueprint = fk.Blueprint('web', os.getenv("APP_NAME"),template_folder='./resources/view',static_folder='./public')

###---------------------------------
### Web routes defenitions goes here
###
###---------------------------------

@web_blueprint.route('/')
def index():
    return route_function_wrapper(HomeController(),'index')()

@web_blueprint.route('/about')
def about():
    return route_function_wrapper(HomeController(),'about')()

@web_blueprint.route('/add_talent',methods=['POST'])
def add_talent():
    return route_function_wrapper(HomeController(),'add_talent')()


@web_blueprint.route('/profile')
@login_required
def profile():
    return fk.stream_template('frontend/profile.html', name = current_user.name)
