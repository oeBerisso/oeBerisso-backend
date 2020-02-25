from flask import redirect, render_template, request, url_for, session, abort, flash
from flask_paginate import Pagination
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.roles import Roles
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from flaskps.models.student import Student
from flaskps.models.reference_api import ReferenceApi
from flaskps.models.gender import Gender
from flaskps.models.town_down import TownDown
from flaskps.models.school import School
from flaskps.models.level import Level
from flaskps.helpers import form_validation
from flaskps.validations import student as student_validation


def new():
    user_permissions = helpers_permission.can_access(["student_new"])

    TownDown.db = get_db()
    Gender.db = get_db()
    School.db = get_db()
    Level.db = get_db()
    configs = config_user()
    types = ReferenceApi.all_documents()
    genders = Gender.all()
    locations = ReferenceApi.all_locations()
    town_downs = TownDown.all()
    schools = School.all()
    levels = Level.all()

    User.db = get_db()
    return render_template("student/new.html", **locals())


def create():
    if helpers_permission.can_access(["student_new"]):
        if not form_validation.validate(student_validation.rules, request.form):
            if validate_student():
                data = request.form
                Student.db = get_db()
                Student.create(data)
                flash("El estudiante se agrego correctamente", "positive")
                return redirect(url_for("student_index"))
            else:
                flash("Estudiante ya existente.", "negative")
                return redirect(url_for("student_new"))
        else:
            return redirect(url_for("student_new"))


def validate_student():
    params = request.form

    Student.db = get_db()
    student = Student.find_by_dni(params["number"])
    return False if student else True


def config_user():
    Configuration.db = get_db()
    return Configuration.all()


def index():

    Student.db = get_db()
    School.db = get_db()
    Level.db = get_db()
    schools = School.all()
    levels = Level.all()
    Roles.db = get_db()
    user_permissions = helpers_permission.can_access(["student_index"])
    if request.args:
        dni = request.args.get("number") or ""
        name = request.args.get("name") or ""
        level = request.args.get("level") or ""
        school = request.args.get("school") or ""
        students = Student.filter(dni, name, level, school)
    else:
        dni = ""
        name = ""
        level = ""
        school = ""
        students = Student.all()

    page = request.args.get("page", type=int, default=1)

    configs = config_user()
    per_page = int(Configuration.get("elementsCount"))
    offset = per_page * (page - 1)
    pagination = Pagination(page=page, per_page=per_page, total=len(students))

    students = students[offset : offset + per_page]

    return render_template("student/index.html", **locals())


def delete(id):
    if helpers_permission.can_access(["student_destroy"]):
        Student.db = get_db()
        Student.delete_student(id)
        flash("El estudiante a sido eliminado correctamente.", "positive")
        return redirect(url_for("student_index"))


def profile(student_id):
    user_permissions = helpers_permission.can_access(["student_update"])
    configs = config_user()
    Student.db = get_db()
    student = Student.show_student(student_id)
    if student is None:
        return redirect(url_for("student_index"))
    else:
        TownDown.db = get_db()
        Gender.db = get_db()
        Roles.db = get_db()
        School.db = get_db()
        Level.db = get_db()
        types = ReferenceApi.all_documents()
        genders = Gender.all()
        locations = ReferenceApi.all_locations()
        town_downs = TownDown.all()
        schools = School.all()
        levels = Level.all()
        return render_template("student/modify.html", **locals())


def modify(student_id):
    if helpers_permission.can_access(["student_update"]):
        if not form_validation.validate(student_validation.rules, request.form):
            Student.db = get_db()
            Student.update(request.form, student_id)
            flash("El estudiante se modifico correctamente.", "positive")
            return redirect(url_for("student_index"))
        else:
            return profile(student_id)
