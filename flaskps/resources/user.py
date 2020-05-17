from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from flask_paginate import Pagination
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.roles import Roles
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from flaskps.helpers import form_validation
from flaskps.validations import register, edit_profile, edit_password
from flask_jwt_extended import create_access_token

def show():
    user_permissions = helpers_permission.can_access()
    User.db = get_db()
    Roles.db = get_db()
    configs = configs_for_user()
    user = User.find_by_username(helper_auth.authenticated(session))
    return render_template(
        "user/profile.html",
        user_permissions=user_permissions,
        user=user,
        configs=configs,
    )


def edit_data():
    if helpers_permission.can_access():
        if not form_validation.validate(edit_profile.rules, request.form):
            User.update(
                helper_auth.authenticated(session),
                request.form["first_name"],
                request.form["last_name"],
                request.form["email"],
            )
            flash("Los datos se actualizaron correctamente", "positive")

        return redirect(url_for("profile"))


def edit_pass():
    if helpers_permission.can_access():
        if not form_validation.validate(edit_password.rules, request.form):
            User.update_password(
                helper_auth.authenticated(session), request.form["password"]
            )
            flash("La contraseña se actualizo correctamente", "positive")
        return redirect(url_for("profile"))


def index():
    user_permissions = helpers_permission.can_access(["users_index"])

    User.db = get_db()
    Roles.db = get_db()

    if request.args:
        name = request.args.get("name") or ""
        username = request.args.get("username") or ""
        email = request.args.get("email") or ""
        active = request.args.get("active") or ""
        users = User.filter(username, name, email, active)
    else:
        name = ""
        email = ""
        username = ""
        active = ""
        users = User.all()
    users = list(map(lambda user: map_roles(user), users))

    page = request.args.get("page", type=int, default=1)

    configs = configs_for_user()
    per_page = int(Configuration.get("elementsCount"))
    offset = per_page * (page - 1)
    pagination_users = users[offset : offset + per_page]
    total = len(users)
    pagination = Pagination(page=page, per_page=per_page, total=len(users))

    return jsonify(
        {
            "users": users,
        }
    )
    # return jsonify(
    # {
    #     "user/index.html",
    #     users=pagination_users,
    #     pagination=pagination,
    #     user_permissions=user_permissions,
    #     configs=configs,
    #     }
    # )


def new():
    if helper_auth.authenticated(session):
        return redirect(url_for("home_page"))

    Configuration.db = get_db()
    configs = configs_for_user()
    if Configuration.service_unavailable():
        abort(503)

    User.db = get_db()
    return render_template("user/new.html", **locals())


def create():
    if not form_validation.validate(register.rules, request.form):
        flash("El usuario se creo correctamente", "positive")
        User.db = get_db()
        User.create(request.form)
        return redirect(url_for("home_page"))
    else:
        return redirect(url_for("user_new"))


def validate_user():
    params = request.form

    User.db = get_db()
    user = User.find_by_username_or_email(params["username"], params["email"])
    return False if user else True


def activate(id):
    if helpers_permission.can_access(["user_update"]):
        User.db = get_db()
        User.change_active(1, id)
        flash("El usuario a sido activo correctamente.", "positive")
        return index()


def desactivate(id):
    if helpers_permission.can_access(["user_update"]):
        User.db = get_db()
        User.change_active(0, id)
        flash("El usuario a sido desactivado correctamente.", "positive")
        return index()


def assign_roles(id):
    if helpers_permission.can_access(["user_update"]):
        User.db = get_db()
        User.delete_roles(id)
        User.modify_roles(id, request.form)
        flash("Los roles del usuario han sido modificados.", "positive")
        return index()


def map_roles(user):
    Roles.db = get_db()
    roles = Roles.all()

    user_roles = User.roles_for_user(user["id"])

    selected_roles = map(
        lambda rol: any(same_role(rol, u_rol) for u_rol in user_roles), roles
    )
    user["roles"] = list(map(compare_roles, roles, selected_roles))

    return user


def compare_roles(rol, boolean):
    rol["selected"] = boolean
    return rol


def same_role(rol1, rol2):
    return rol1["id"] == rol2["roleid"]


def configs_for_user():
    Configuration.db = get_db()
    return Configuration.all()
