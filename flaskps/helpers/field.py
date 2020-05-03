from flaskps.models.user import User
from flaskps.db import get_db
from flask import flash
import re


def compare_fields(js, field1, name1, field2, name2):
    if field1 != field2:
        message = (
            "El campo " + str(name1) + " y el campo " + str(name2) + " no coinciden"
        )
        if js: return message

        flash(message, "negative")
        return 1
    else:
        return 0


def min_length(js, field, name, length):
    if len(field) < length:
        message = "El campo " + str(name) + " no posee el tamaño minimo"
        if js: return message

        flash(message, "negative")
        return 1
    else:
        return 0


def max_length(js, field, name, length):
    if len(field) > length:
        message = "El campo " + str(name) + " supera el tamaño maximo"
        if js: return message

        flash(message, "negative")
        return 1
    else:
        return 0


def email(js, field):
    regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if not re.search(regex, field):
        if js: return "El formato del mail no es valido"

        flash("El formato del mail no es valido", "negative")
        return 1
    else:
        return 0


def presence(js, field, name):
    if len(field):
        return 0
    else:
        message = "El campo " + str(name) + " es requerido"
        if js: return message

        flash(message, "negative")
        return 1


def unique_mail(js, field, username=""):
    User.db = get_db()
    user = User.find_by_email(field)
    if user != None and user["username"] != username:
        if js: return "El mail que intenta utilizar ya existe"

        flash("El mail que intenta utilizar ya existe", "negative")
        return 1
    else:
        return 0


def unique_user(js, field):
    User.db = get_db()
    user = User.find_by_username(field)
    if user != None:
        if js: return "El usuario que intenta utilizar ya existe"

        flash("El usuario que intenta utilizar ya existe", "negative")
        return 1
    else:
        return 0


def type_number(js, field, name):
    try:
        float(field)
        return 0
    except ValueError:
        message = "El campo " + str(name) + " tiene que ser un numero"
        if js: return message

        flash(message, "negative")
        return 1
