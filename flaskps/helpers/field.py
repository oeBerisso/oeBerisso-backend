from flaskps.models.user import User
from flaskps.db import get_db
from flask import flash
import re


def compare_fields(field1, name1, field2, name2):
    if field1 != field2:
        message = (
            "El campo " + str(name1) + " y el campo " + str(name2) + " no coinciden"
        )
        flash(message, "negative")
        return 1
    else:
        return 0


def min_length(field, name, length):
    if len(field) < length:
        message = "El campo " + str(name) + " no posee el tamaño minimo"
        flash(message, "negative")
        return 1
    else:
        return 0


def max_length(field, name, length):
    if len(field) > length:
        message = "El campo " + str(name) + " supera el tamaño maximo"
        flash(message, "negative")
        return 1
    else:
        return 0


def email(field):
    regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if not re.search(regex, field):
        flash("El formato del mail no es valido", "negative")
        return 1
    else:
        return 0


def presence(field, name):
    if len(field):
        return 0
    else:
        message = "El campo " + str(name) + " es requerido"
        flash(message, "negative")
        return 1


def unique_mail(field, username=""):
    User.db = get_db()
    user = User.find_by_email(field)
    if user != None and user["username"] != username:
        flash("El mail que intenta utilizar ya existe", "negative")
        return 1
    else:
        return 0


def unique_user(field):
    User.db = get_db()
    user = User.find_by_username(field)
    if user != None:
        flash("El usuario que intenta utilizar ya existe", "negative")
        return 1
    else:
        return 0


def type_number(field, name):
    try:
        float(field)
        return 0
    except ValueError:
        message = "El campo " + str(name) + " tiene que ser un numero"
        flash(message, "negative")
        return 1
