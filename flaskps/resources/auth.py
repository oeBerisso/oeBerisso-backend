from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from flaskps.helpers import form_validation
from flaskps.validations import auth


def login():
    if helper_auth.authenticated(session):
        return redirect(url_for("home_page"))

    Configuration.db = get_db()
    configs = Configuration.all()

    return render_template("auth/login.html", **locals())


def authenticate():
    params = request.form
    if not form_validation.validate(auth.rules, params):
        User.db = get_db()
        user = User.find_by_username_and_pass(params["username"], params["password"])
        if not user:
            flash("Usuario o clave incorrecto.", "negative")
            return redirect(url_for("auth_login"))
        if user["active"] == 0:
            flash("El usuario no se encuentra activo.", "negative")
            return redirect(url_for("auth_login"))

        session["user"] = user["username"]
        flash("La sesión se inició correctamente.", "positive")

        return redirect(url_for("home_page"))
    else:
        return redirect(url_for("auth_login"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.", "positive")

    return redirect(url_for("auth_login"))
