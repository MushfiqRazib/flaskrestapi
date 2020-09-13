from flask_restx import Api
from flask import Blueprint

from .main.controller.fib_controller import api as fib_ns
from .main.controller.health_controller import api as health_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='PYTHON FLASK REST API TASK',
          version='1.0',
          description='a task for flask restplus web service'
          )

api.add_namespace(fib_ns, path='/fib')
api.add_namespace(health_ns)