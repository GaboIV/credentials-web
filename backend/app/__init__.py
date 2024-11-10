from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config
import MySQLdb

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

    with app.app_context():
        from app.controllers import credentials_controller
        app.register_blueprint(credentials_controller)

    return app