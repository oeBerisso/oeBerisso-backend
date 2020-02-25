from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.models.user import User
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission


def index():

    user_permissions = helpers_permission.can_access("config_index")

    Configuration.db = get_db()
    Roles.db = get_db()

    configs = Configuration.all()
    return render_template("admin/index.html", **locals())


def update():
    helpers_permission.can_access("config_update")

    Configuration.db = get_db()

    form = request.form.copy()
    if not form:
        abort(404)

    if "maintenance" in form:
        form["maintenance"] = "1"
    else:
        form["maintenance"] = "0"

    errors = Configuration.updateAll(form)

    flash("La configuracion fue actualizada correctamente", "positive")
    return redirect(url_for("admin_index"))
