import MySQLdb
import logging
from flask import Flask
from flask_cors import CORS
from app.config import Config
from flask_jwt_extended import JWTManager

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

db = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/auth/*": {"origins": "http://localhost:4200"}})
    jwt = JWTManager(app)

    global db
    db = MySQLdb.connect(
        host=app.config["DB_HOST"],
        user=app.config["DB_USER"],
        passwd=app.config["DB_PASS"],
        db=app.config["DB_NAME"]
    )

    # Registrando el Blueprint
    with app.app_context():
        from app.controllers import credentials_controller
        app.register_blueprint(credentials_controller.credentials_controller, url_prefix='/auth')  # Opcional: agregar un prefijo

    return app
