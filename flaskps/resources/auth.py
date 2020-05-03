from flask import jsonify, session, request
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.helpers import form_validator
from flaskps.validations import register

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
