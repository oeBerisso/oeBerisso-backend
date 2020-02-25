from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.roles import Roles
from flaskps.models.workshop import Workshop
from flaskps.models.school_year import SchoolYear
from flaskps.models.teacher import Teacher
from flaskps.models.student import Student
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission


def index():

    user_permissions = helpers_permission.can_access("workshop_index")

    Configuration.db = get_db()
    Roles.db = get_db()
    Workshop.db = get_db()

    workshops = Workshop.all()
    configs = Configuration.all()
    return render_template("workshop/index.html", **locals())


def assign_view(workshop_id):
    user_permissions = helpers_permission.can_access("workshop_update")

    Configuration.db = get_db()
    Roles.db = get_db()
    Workshop.db = get_db()
    Teacher.db = get_db()

    configs = Configuration.all()

    teachers = Teacher.all()
    schoolar_years = Workshop.getSchollarYears(workshop_id)
    workshop_data = Workshop.getData(workshop_id)
    return render_template("workshop/assign_professors.html", **locals())


def assign(workshop_id, school_year_id):
    helpers_permission.can_access("workshop_update")
    Workshop.db = get_db()
    Teacher.db = get_db()
    teachers = request.form.getlist("teachers")

    if len(teachers) == 0:
        flash("Debe quedar almenos un docente asignado al taller", "negative")
    else:
        Workshop.removeTeachers(workshop_id, school_year_id)
        Teacher.assign_workshop(teachers, workshop_id, school_year_id)
        flash("Los docentes asignados fueron modificados correctamente!", "positive")

    return redirect(url_for("workshop_assign_view", workshop_id=workshop_id))


def assign_students(workshop_id, school_year_id):
    helpers_permission.can_access("workshop_update")
    Workshop.db = get_db()
    Student.db = get_db()

    students = request.form.getlist("students")

    Workshop.delete_students_for(workshop_id, school_year_id)
    Workshop.assign_students_to(workshop_id, school_year_id, students)
    flash("Se modificaron los estudiantes asignados correctamente", "positive")
    return redirect(
        url_for(
            "workshop_students", workshop_id=workshop_id, school_year_id=school_year_id
        )
    )


def students(workshop_id):
    user_permissions = helpers_permission.can_access("workshop_update")
    Workshop.db = get_db()
    Student.db = get_db()
    SchoolYear.db = get_db()
    Configuration.db = get_db()
    Roles.db = get_db()

    configs = Configuration.all()
    workshop_data = Workshop.getData(workshop_id)
    schoolar_years = SchoolYear.assignedToWorkshop(workshop_id)

    if not len(schoolar_years):
        abort(404)

    all_students = Student.all()
    return render_template("workshop/assign_students.html", **locals())
