from flask import Flask
from flask_cors import CORS
from flask_restx import Api

app = Flask(__name__)
CORS(app)

api = Api(app, version='1.0', title='CSV API',doc='/swagger/')


from src.main.routes.atendimentos_routes import api as atendimentos_ns
api.add_namespace(atendimentos_ns, path='/api/v1/atendimentos')