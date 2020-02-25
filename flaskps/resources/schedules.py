from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.user import User
from flaskps.models.workshop import Workshop
from flaskps.models.cores import Cores
from flaskps.models.days import Days
from flaskps.models.school_year import SchoolYear
from flaskps.models.schedules import Schedules
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission


def index():

    user_permissions = helpers_permission.can_access("schedules_index")

    Schedules.db = get_db()
    Configuration.db = get_db()
    Days.db = get_db()
    SchoolYear.db = get_db()

    configs = Configuration.all()
    all_schedules = Schedules.allWithData()

    all_schoolar_years = SchoolYear.allWithWorkshop()

    all_schedules_parsed = [
        {
            "start_date": school_year["start_date"],
            "ending_date": school_year["ending_date"],
            "semester": school_year["semester"],
            "list": Schedules.allBySchoolarYear(school_year["id"]),
        }
        for school_year in all_schoolar_years
    ]

    return render_template("schedules/index.html", **locals())


def new():
    user_permissions = helpers_permission.can_access("schedules_new")

    Configuration.db = get_db()
    Workshop.db = get_db()
    Cores.db = get_db()
    Days.db = get_db()

    days = Days.all()
    configs = Configuration.all()
    workshops_assigned = Workshop.allAssignedToSchollarYear()
    cores = Cores.all()

    return render_template("schedules/new.html", **locals())


def create():
    user_permissions = helpers_permission.can_access("schedules_new")
    Configuration.db = get_db()
    Schedules.db = get_db()

    workshop = request.form.get("workshop")
    core = request.form.get("core")
    day = request.form.get("day")
    start_time = request.form.get("start_time")
    finish_time = request.form.get("finish_time")
    # raise Exception(request.form)

    # Schedules.resetSchedule(workshop, core)
    if Schedules.findAssigment(workshop, core, day, start_time, finish_time):
        flash("Hay un horario asignado para este curso para este curso", "negative")
        return redirect((url_for("schedules_new")))
    Schedules.setAllDays(workshop, core, day, start_time, finish_time)
    flash("Los horarios se cargaron correctamente", "positive")

    return redirect(url_for("schedules_index"))
