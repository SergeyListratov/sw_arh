from flask_restx import Api
from flask import Blueprint

from .main.controller.switch_controller import api as switch_ns
from .main.controller.switch_details_controller import api as switch_details_ns
from .main.controller.switch_download_controller import api as switch_download_ns
from .main.controller.auth_controller import api as auth_ns


blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
    version='1.0',
    description='a boilerplate for flask restplus (restx) web service',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(switch_ns, path='/api/switches')
api.add_namespace(switch_details_ns, path='/api/switches')
api.add_namespace(switch_download_ns, path='/api/switches')
api.add_namespace(auth_ns, path='/api/auth')
