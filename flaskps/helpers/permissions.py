from flask import session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.models.user import User
from flaskps.helpers import auth as helper_auth


def has_permission(user_roles, page_roles):
    if len(page_roles):
        return any(x in page_roles for x in user_roles)
    else:
        return True


def can_access(permissions_required=[]):

    Configuration.db = get_db()
    Roles.db = get_db()
    User.db = get_db()
    if helper_auth.authenticated(session):

        user_permissions = Roles.getUserPermissions(helper_auth.authenticated(session))
        if Configuration.service_unavailable() and not (
            has_permission(user_permissions, ["config_update"])
            and has_permission(user_permissions, ["config_index"])
        ):
            abort(503)

        if not User.is_active(helper_auth.authenticated(session)):
            del session["user"]
            session.clear()
            flash("El usuario fue deshabilitado por un administrador", "negative")
            abort(403)

        if not has_permission(user_permissions, permissions_required):
            abort(403)

    else:
        abort(403)

    return user_permissions
