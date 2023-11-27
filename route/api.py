from flask import Blueprint
from core.route.route_helper import route_function_wrapper
api_blueprint = Blueprint('api', __name__)

###---------------------
### API routes defenitions goes here
###
###---------------------


# @api_blueprint.route('/first')
# def about():
#     return route_function_wrapper()