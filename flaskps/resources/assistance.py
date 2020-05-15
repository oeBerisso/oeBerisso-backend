from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.user import User
from flaskps.models.schedules import Schedules
from flaskps.models.school_year import SchoolYear
from flaskps.models.workshop import Workshop
from flaskps.models.assistance import Assistance
from flaskps.models.student import Student
from flaskps.models.user import User
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from flaskps.models.configuration import Configuration


def index():
    user_permissions = helpers_permission.can_access("assistace_list")
    Configuration.db = get_db()
    configs = Configuration.all()
    SchoolYear.db = get_db()
    school_year = SchoolYear.search_date()
    Workshop.db = get_db()
    if school_year: workshops = Workshop.getFromSchoolYear(school_year["id"])

    return render_template("assistance/index.html", **locals())


def workshop_view(school_year_id):
    user_permissions = helpers_permission.can_access("assistace_list")

    Workshop.db = get_db()
    workshops = Workshop.getFromSchoolYear(school_year_id)
    return workshops


def date_select(school_year_id, workshop_id):
    user_permissions = helpers_permission.can_access("assistace_list")
    Configuration.db = get_db()
    SchoolYear.db = get_db()
    configs = Configuration.all()
    school_year = SchoolYear.search_date()

    return render_template("assistance/date.html", **locals())


def schedules_view(school_year_id, workshop_id):
    user_permissions = helpers_permission.can_access("assistace_list")

    Configuration.db = get_db()
    Student.db = get_db()
    Assistance.db = get_db()

    dateSelected = request.args.get("date")

    if not dateSelected:
        return redirect(
            url_for(
                "as_date_view", school_year_id=school_year_id, workshop_id=workshop_id
            )
        )

    assistances = {
        a["student_id"]: a
        for a in Assistance.getAllFromDate(school_year_id, workshop_id, dateSelected)
    }

    # raise Exception(assistances)

    configs = Configuration.all()
    assistance = Assistance.all()
    students = Student.data_get_assigned_to(workshop_id, school_year_id)

    return render_template("assistance/school_year.html", **locals())


def create(school_year_id, workshop_id):
    user_permissions = helpers_permission.can_access("assistace_update")

    Assistance.db = get_db()
    date = request.args.get("date")
    students = request.form
    Assistance.removeAllFrom(school_year_id, workshop_id, date)
    Assistance.createAll(school_year_id, workshop_id, date, students)

    flash("Se guardo la asistencia", "positive")
    return redirect(
        url_for(
            "as_schedules_view",
            school_year_id=school_year_id,
            workshop_id=workshop_id,
            date=date,
        )
    )
