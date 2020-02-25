from flask import redirect, render_template, request, url_for, session, abort, flash
from flask_paginate import Pagination
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.roles import Roles
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from flaskps.models.reference_api import ReferenceApi
from flaskps.models.gender import Gender
from flaskps.models.town_down import TownDown
from flaskps.models.school import School
from flaskps.models.level import Level
from flaskps.models.teacher import Teacher
from flaskps.helpers import form_validation
from flaskps.validations import teacher as teacher_validation


def new():
    user_permissions = helpers_permission.can_access(["teacher_new"])
    Gender.db = get_db()
    configs = configs_for_user()
    types = ReferenceApi.all_documents()
    genders = Gender.all()
    locations = ReferenceApi.all_locations()

    return render_template("teacher/new.html", **locals())


def create():
    if helpers_permission.can_access(["teacher_new"]):
        if not form_validation.validate(teacher_validation.rules, request.form):
            if validate_teacher():
                data = request.form
                Teacher.db = get_db()
                Teacher.create(data)
                flash("El Profesor se agrego correctamente", "positive")
                return redirect(url_for("teacher_index"))
            else:
                flash("El Profesor ya existente.", "negative")
                return redirect(url_for("teacher_new"))
        else:
            return redirect(url_for("teacher_new"))


def validate_teacher():
    params = request.form
    Teacher.db = get_db()
    teacher = Teacher.find_by_dni(params["number"])
    return False if teacher else True


def configs_for_user():
    Configuration.db = get_db()
    return Configuration.all()


def index():

    user_permissions = helpers_permission.can_access(["teacher_index"])

    Teacher.db = get_db()
    if request.args:
        dni = request.args.get("number") or ""
        name = request.args.get("name") or ""
        teachers = Teacher.filter(dni, name)
    else:
        dni = ""
        name = ""
        teachers = Teacher.all()

    page = request.args.get("page", type=int, default=1)

    configs = configs_for_user()
    per_page = int(Configuration.get("elementsCount"))
    offset = per_page * (page - 1)
    pagination = Pagination(page=page, per_page=per_page, total=len(teachers))

    teachers = teachers[offset : offset + per_page]

    return render_template("teacher/index.html", **locals())


def delete(id):
    if helpers_permission.can_access(["teacher_destroy"]):
        Teacher.db = get_db()
        Teacher.delete_teacher(id)
        flash("El profesor a sido eliminado correctamente.", "positive")
        return redirect(url_for("teacher_index"))


def profile(teacher_id):
    user_permissions = helpers_permission.can_access(["teacher_show"])
    configs = configs_for_user()
    Teacher.db = get_db()
    teacher = Teacher.show_teacher(teacher_id)
    if teacher is None:
        return redirect(url_for("teacher_index"))
    else:
        Gender.db = get_db()
        Roles.db = get_db()
        configs = configs_for_user()
        types = ReferenceApi.all_documents()
        genders = Gender.all()
        locations = ReferenceApi.all_locations()
        return render_template("teacher/modify.html", **locals())


def modify(teacher_id):
    if helpers_permission.can_access(["teacher_update"]):
        if not form_validation.validate(teacher_validation.rules, request.form):
            Teacher.db = get_db()
            Teacher.update(request.form, teacher_id)
            flash("El profesor se modifico correctamente.", "positive")
            return redirect(url_for("teacher_index"))
        else:
            return profile(teacher_id)
