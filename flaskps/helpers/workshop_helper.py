from flaskps.db import get_db
from flaskps.models.workshop import Workshop
from flaskps.models.student import Student


def in_schoolar_year(workshop_id, schoolar_year_id):
    Workshop.db = get_db()
    return Workshop.getTeachersFrom(workshop_id, schoolar_year_id)


def is_assigned(workshop_id, schoolar_year_id, teacher_id):
    Workshop.db = get_db()
    assigned = Workshop.isAssigned(workshop_id, schoolar_year_id, teacher_id)
    return len(assigned)


def workshop_in_school_year(workshop_id, school_year_id):
    Workshop.db = get_db()
    in_schoolar_year = Workshop.allInSchoolYear(workshop_id, school_year_id)
    return len(in_schoolar_year)


def is_student_assigned(student, workshop_id, school_year_id):
    Student.db = get_db()
    return student in Student.get_id_assigned_to(workshop_id, school_year_id)


def asigned_to_schoolar_year(workshop_id):
    Workshop.db = get_db()
    return len(Workshop.isInSchoolYear(workshop_id))
