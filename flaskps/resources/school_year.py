from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.models.user import User
from flaskps.models.school_year import SchoolYear
from flaskps.models.workshop import Workshop
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from flaskps.helpers import form_validation
from flaskps.validations import create_school_year


def new():
    Configuration.db = get_db()
    Roles.db = get_db()
    user_permissions = helpers_permission.can_access("school_year_new")
    configs = Configuration.all()

    return render_template("school_year/index.html", **locals())


def create():
    Configuration.db = get_db()
    Roles.db = get_db()
    SchoolYear.db = get_db()

    user_permissions = helpers_permission.can_access("school_year_new")
    form = request.form.copy()
    semester = request.form.get("semester")

    if not form or not form_validation.validate(create_school_year.rules, form):
        if form["start_date"] > form["ending_date"]:
            flash(
                "la fecha de inicio debe ser anterior a la de fin del semestre",
                "negative",
            )
            return redirect(url_for("school_year_new"))

        if SchoolYear.validateInterval(form["start_date"], form["ending_date"]):
            flash(
                "La fecha de inicio o fin se superpone con otro ciclo lectivo",
                "negative",
            )
            return redirect(url_for("school_year_new"))

        SchoolYear.create(semester, form["start_date"], form["ending_date"])
        flash("El ciclo lectivo se cargo correctamente", "positive")
        return redirect(url_for("school_year_new"))
    else:
        return redirect(url_for("school_year_new"))


def list():
    Configuration.db = get_db()
    Roles.db = get_db()
    SchoolYear.db = get_db()
    Workshop.db = get_db()

    configs = Configuration.all()
    workshops_lines = Workshop.allInLines(3)
    user_permissions = helpers_permission.can_access("school_year_show")
    form = request.form.copy()

    schoolarYears = SchoolYear.all()

    return render_template("school_year/list.html", **locals())


def assignWorkshops(schoolar_year_id):
    Configuration.db = get_db()
    Roles.db = get_db()
    SchoolYear.db = get_db()
    Workshop.db = get_db()

    user_permissions = helpers_permission.can_access("school_year_update")
    configs = Configuration.all()
    Workshop.assignWorkshopsTo(request.form, schoolar_year_id)
    flash("Los talleres asignados fueron modificados correctamente", "positive")
    return redirect(url_for("school_year_list"))
