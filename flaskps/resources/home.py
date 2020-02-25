from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.models.user import User
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from datetime import datetime


def index():
    Configuration.db = get_db()
    Roles.db = get_db()
    User.db = get_db()

    user_permissions = Roles.getUserPermissions(
        helper_auth.authenticated(session) or ""
    )

    if Configuration.service_unavailable():
        abort(503)

    if helper_auth.authenticated(session) and not User.is_active(
        helper_auth.authenticated(session)
    ):
        del session["user"]
        session.clear()
        flash("El usuario fue deshabilitado por un administrador", "negative")
        abort(403)

    title = Configuration.get("title")
    configs = Configuration.all()
    return render_template("home.html", **locals())
