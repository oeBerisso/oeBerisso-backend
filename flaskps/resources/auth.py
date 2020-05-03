<<<<<<< HEAD
from flask import jsonify, session, request, redirect
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.config import Config
from flaskps.helpers import form_validator
from flaskps.validations import register

import requests

def google_login(client):
    # Find out what URL to hit for Google login
    google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()

    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

def create():
    if not form_validator.validate(register.rules, request.json):
        User.db = get_db()
        User.create(request.json)
        return jsonify({"response":"todo pillo"}), 200
    else:
        return jsonify({"response":"toca de aca"}), 422


def login(request, create_access_token):
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    User.db = get_db()
    user = User.find_by_username_and_pass(username, password)
    status = True
    msg = ""

    if not user:
        msg = "Usuario o clave incorrecto."
        status = False
    if status and user["active"] == 0:
        msg = "El usuario no se encuentra activo."
        status = False

    if status:
        msg = "La sesión se inició correctamente."

    return jsonify(
        {
            "status": status,
            msg: msg,
            "token": create_access_token(identity=user["username"]),
        }
    )
