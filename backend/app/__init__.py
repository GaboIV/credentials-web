import logging
from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config
import MySQLdb

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,  # Nivel de log (INFO, DEBUG, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
    handlers=[
        logging.StreamHandler()  # Muestra los logs en la consola
    ]
)

db = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
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
