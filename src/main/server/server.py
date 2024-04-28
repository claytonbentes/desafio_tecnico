from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connection_handler
db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

from src.main.routes.atendimentos_routes import atendimentos_route_bp
app.register_blueprint(atendimentos_route_bp)