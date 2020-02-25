from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission


def forbbiden(code):
    Configuration.db = get_db()
    Roles.db = get_db()
    user_permissions = Roles.getUserPermissions(
        helper_auth.authenticated(session) or ""
    )
    configs = Configuration.all()
    return render_template("error/403.html", **locals())


def service_unavailable(code):
    Configuration.db = get_db()
    Roles.db = get_db()
    user_permissions = Roles.getUserPermissions(
        helper_auth.authenticated(session) or ""
    )
    configs = Configuration.all()
    return render_template("error/503.html", **locals())


def page_not_found(code):
    Configuration.db = get_db()
    Roles.db = get_db()
    user_permissions = Roles.getUserPermissions(
        helper_auth.authenticated(session) or ""
    )
    configs = Configuration.all()
    return render_template("error/404.html", **locals())
