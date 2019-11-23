from flask_restplus import Api
from flask import Flask, Blueprint
#from app import app

from app.apis.demo import api as demo_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(demo_ns, path='/demo')