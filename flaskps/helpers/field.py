from flaskps.models.user import User
from flaskps.db import get_db
from flask import flash
import re


def compare_fields(js, field1, name1, field2, name2):
    if field1 != field2:
        message = (
            "El campo " + str(name1) + " y el campo " + str(name2) + " no coinciden"
        )
        if js: return "No coincide con el campo " + str(name2)

        flash(message, "negative")
        return 1
    else:
        return 0


def min_length(js, field, name, length):
    if len(field) < length:
        message = "El campo " + str(name) + " no posee el tamaño minimo de " + str(length) + " caracteres"
        if js: return "No posee el tamaño minimo de " + str(length) + " caracteres"

        flash(message, "negative")
        return 1
    else:
        return 0


def max_length(js, field, name, length):
    if len(field) > length:
        message = "El campo " + str(name) + " supera el tamaño maximo de " + str(length) + " caracteres"
        if js: return "Supera el tamaño maximo de " + str(length) + " caracteres"

        flash(message, "negative")
        return 1
    else:
        return 0

def not_google_username(js, field):
    regex= "^g_"
    if re.search(regex, field):
        if js: return "El prefijo g_ no puede ser utilizado por usuarios"

        flash("El prefijo g_ no puede ser utilizado por usuarios", "negative")
        return 1
    else:
        return 0


def email(js, field):
    regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    if not re.search(regex, field):
        if js: return "El formato del mail no es valido"

        flash("El formato no es valido", "negative")
        return 1
    else:
        return 0


def presence(js, field, name):
    if len(field):
        return 0
    else:
        message = "El campo " + str(name) + " es requerido"
        if js: return "El campo es requerido"

        flash(message, "negative")
        return 1


def unique_mail(js, field, username=""):
    User.db = get_db()
    user = User.find_by_email(field)
    if user != None and user["username"] != username:
        if js: return "Este mail ya se encuentra registrado"

        flash("El mail que intenta utilizar ya existe", "negative")
        return 1
    else:
        return 0


def unique_user(js, field):
    User.db = get_db()
    user = User.find_by_username(field)
    if user != None:
        if js: return "Este usuario ya se encuentra registrado"

        flash("El usuario que intenta utilizar ya existe", "negative")
        return 1
    else:
        return 0


def type_number(js, field, name):
    try:
        float(field)
        return 0
    except ValueError:
        message = "El campo " + str(name) + " debe ser un numero"
        if js: return "Debe ser un valor numerico"

        flash(message, "negative")
        return 1
