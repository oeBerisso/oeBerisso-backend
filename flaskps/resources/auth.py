from flask import jsonify, session, request, redirect
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.config import Config
from flaskps.helpers import form_validator
from flaskps.validations import register
import json

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

def google_callback(client):
    User.db = get_db()

    code = request.args.get("code")
    google_provider_cfg = requests.get(Config.GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(Config.GOOGLE_CLIENT_ID, Config.GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    
    # raise Exception(userinfo_response.json())
    response = userinfo_response.json()
    
    user = User.find_by_email(response["email"])
    is_new = False
    status = True
    if not user:
        # google => oeberisso
        # ------------------------
        # given_name => first_name
        # family_name => last_name
        # email => email

        username, dom = response["email"].split('@')
        User.create_from_google(response["email"], username, response["given_name"], response["family_name"])
        msg = "Se creo el usuario"
        is_new = True

    if not is_new and status and user["active"] == 0:
        msg = "El usuario no se encuentra activo."
        status = False

    if status:
        session["user"] = username if is_new else user["username"]
        if not is_new:
            msg = "La sesión se inició correctamente."

    return jsonify(
        {
            "status": status,
            "msg": msg,
            "username": session["user"],
            "email": response["email"],
        }
    )


def create():
    errors = form_validator.validate(register.rules, request.json, True)
    if not errors:
        User.db = get_db()
        User.create(request.json)
        return jsonify({}), 201
    else:
        return jsonify({"errors": errors}), 422


def login(request, create_access_token):
    data = request.get_json()
    User.db = get_db()
    user = User.find_by_username_and_pass(data["username"], data["password"])

    if not user:
        return jsonify({"msg":"Usuario o clave incorrecto."}), 422

    if user["active"] == 0:
        return jsonify({"msg":"El usuario no se encuentra activo."}), 422

    return jsonify(
        {
            "msg": "La sesión se inició correctamente.",
            "token": create_access_token(identity=user["username"]),
        }
    )
