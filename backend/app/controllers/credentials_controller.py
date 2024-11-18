import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token
from app import db

credentials_controller = Blueprint("credentials_controller", __name__)

@credentials_controller.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Agregar log para verificar lo que recibes
    logging.info(f"Login attempt with username: {username} and password: {password}")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    db.commit()
    cursor.close()

    # Agregar log para ver el resultado del query
    logging.info(f"User found: {user}")

    if user:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Credenciales incorrectas"}), 401

@credentials_controller.route('/get_credentials', methods=['GET'])
@jwt_required()
def get_credentials():
    cursor = db.cursor()
    cursor.execute("SELECT id, name, encrypt_value FROM credentials")
    credentials = cursor.fetchall()
    db.commit()
    cursor.close()
    return jsonify(credentials=[{"id": cred[0], "name": cred[1], "encrypt_value": cred[2]} for cred in credentials])
