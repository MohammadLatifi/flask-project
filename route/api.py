from flask import Blueprint
from core.route.route_helper import route_function_wrapper
import os


api_blueprint = Blueprint('api', os.getenv("APP_NAME"))
###---------------------
### API routes defenitions goes here
###
###---------------------


# @api_blueprint.route('/first')
# def about():
#     return route_function_wrapper()