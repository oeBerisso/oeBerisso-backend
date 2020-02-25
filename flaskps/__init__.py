from os import path
from flask import Flask, render_template, g, session
from flaskps.db import get_db
from flaskps.models.roles import Roles
from flaskps.helpers import auth as helper_auth
from flask_session import Session
from flaskps.models.configuration import Configuration
from flaskps.resources import (
    user,
    admin,
    auth,
    home,
    error,
    student,
    school_year,
    workshop,
    teacher,
    schedules,
    instrument,
    assistance,
    map_point,
)
from flaskps.config import Config
from flaskps.helpers import (
    auth as helper_auth,
    bind_filters,
    permissions,
    maintenance,
    workshop_helper,
)


app = Flask(__name__)
app.config.from_object(Config)

app.register_error_handler(403, error.forbbiden)
app.register_error_handler(404, error.page_not_found)
app.register_error_handler(503, error.service_unavailable)


bind_filters.bind_template_filters(app)

# Server Side session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(
    is_authenticated=helper_auth.authenticated,
    has_permission=permissions.has_permission,
    must_be_closed=maintenance.must_be_closed,
    in_schoolar_year=workshop_helper.in_schoolar_year,
    is_assigned=workshop_helper.is_assigned,
    workshop_in_school_year=workshop_helper.workshop_in_school_year,
    is_student_assigned=workshop_helper.is_student_assigned,
    asigned_to_schoolar_year=workshop_helper.asigned_to_schoolar_year,
)


# Autenticación
app.add_url_rule("/login", "auth_login", auth.login)
app.add_url_rule("/logout", "auth_logout", auth.logout)
app.add_url_rule(
    "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
)

# Profesores
app.add_url_rule(
    "/registrar_profesor", "teacher_create", teacher.create, methods=["POST"]
)
app.add_url_rule("/registrar_profesor", "teacher_new", teacher.new)


app.add_url_rule("/profesores", "teacher_index", teacher.index, methods=["GET"])
app.add_url_rule(
    "/profesor/<teacher_id>/perfil",
    "teacher_<teacher_id>_profile",
    teacher.profile,
    methods=["GET"],
)
app.add_url_rule(
    "/profesor/<teacher_id>/modificar",
    "teacher_<teacher_id>_edit",
    teacher.modify,
    methods=["POST"],
)
app.add_url_rule(
    "/profesor/<id>/eliminar", "teacher_<id>_remove", teacher.delete, methods=["GET"]
)

# Instrumentos
app.add_url_rule(
    "/registrar_instrumento", "instrument_create", instrument.create, methods=["POST"]
)
app.add_url_rule("/registrar_instrumento", "instrument_new", instrument.new)


app.add_url_rule("/instrumentos", "instrument_index", instrument.index, methods=["GET"])
app.add_url_rule(
    "/instrumento/<instrument_id>/perfil",
    "instrument_<instrument_id>_profile",
    instrument.profile,
    methods=["GET"],
)
app.add_url_rule(
    "/instrumento/<instrument_id>/modificar",
    "instrument_<instrument_id>_edit",
    instrument.modify,
    methods=["POST"],
)
app.add_url_rule(
    "/instrumento/<id>/eliminar",
    "instrument_<id>_remove",
    instrument.delete,
    methods=["GET"],
)
# Estudiantes
app.add_url_rule(
    "/registrar_alumno", "student_create", student.create, methods=["POST"]
)
app.add_url_rule("/registrar_alumno", "student_new", student.new)
app.add_url_rule("/estudiantes", "student_index", student.index, methods=["GET"])
app.add_url_rule(
    "/estudiante/<student_id>/modificar",
    "student_<student_id>_edit",
    student.modify,
    methods=["POST"],
)
app.add_url_rule(
    "/estudiante/<id>/eliminar", "student_<id>_remove", student.delete, methods=["GET"]
)
app.add_url_rule(
    "/estudiante/<student_id>/perfil",
    "student_<student_id>_profile",
    student.profile,
    methods=["GET"],
)

# Usuarios
app.add_url_rule("/usuarios", "user_index", user.index, methods=["GET"])
app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
app.add_url_rule("/registrarse", "user_new", user.new)
app.add_url_rule(
    "/usuarios/<id>/activar", "user_<id>_activate", user.activate, methods=["POST"]
)
app.add_url_rule(
    "/usuarios/<id>/desactivar",
    "user_<id>_desactivate",
    user.desactivate,
    methods=["POST"],
)
app.add_url_rule(
    "/usuarios/<id>/modicar_roles",
    "user_<id>_roles",
    user.assign_roles,
    methods=["POST"],
)
app.add_url_rule("/perfil", "profile", user.show, methods=["GET"])
app.add_url_rule("/editar_perfil", "edit_profile", user.edit_data, methods=["POST"])
app.add_url_rule("/editar_contraseña", "edit_pass", user.edit_pass, methods=["POST"])

# Ciclo Lectivo
app.add_url_rule("/ciclo_lectivo", "school_year_new", school_year.new)
app.add_url_rule(
    "/ciclo_lectivo/<schoolar_year_id>/asignar",
    "school_year_assing_workshops",
    school_year.assignWorkshops,
    methods=["POST"],
)
app.add_url_rule("/ciclo_lectivo/lista", "school_year_list", school_year.list)
app.add_url_rule(
    "/ciclo_lectivo_nuevo",
    "school_year_create",
    school_year.create,
    methods=["GET", "POST"],
)

# Talleres
app.add_url_rule("/talleres", "workshop_index", workshop.index)
app.add_url_rule(
    "/taller/<workshop_id>/estudiantes", "workshop_students", workshop.students
)
app.add_url_rule(
    "/taller/<workshop_id>/<school_year_id>/asignar_estudiantes",
    "workshop_assign_students",
    workshop.assign_students,
    methods=["POST"],
)
app.add_url_rule(
    "/taller/<workshop_id>/asignar_docentes",
    "workshop_assign_view",
    workshop.assign_view,
)
app.add_url_rule(
    "/taller/<workshop_id>/<school_year_id>/asignar",
    "workshop_assign",
    workshop.assign,
    methods=["POST"],
)

# Puntos del mapa
app.add_url_rule("/puntos", "points", map_point.index)


# Schedules
app.add_url_rule("/horarios", "schedules_index", schedules.index)
app.add_url_rule("/horarios/nuevo", "schedules_new", schedules.new)
app.add_url_rule(
    "/horarios/nuevo", "schedules_create", schedules.create, methods=["POST"]
)

# Asistencia
app.add_url_rule("/asistencia", "assistance_index", assistance.index)
app.add_url_rule(
    "/asistencia/<school_year_id>/ver", "as_workshop_view", assistance.workshop_view
)
app.add_url_rule(
    "/asistencia/<school_year_id>/<workshop_id>/ver",
    "as_schedules_view",
    assistance.schedules_view,
)
app.add_url_rule(
    "/asistencia/<school_year_id>/<workshop_id>/fecha",
    "as_date_view",
    assistance.date_select,
)

app.add_url_rule(
    "/asistencia/<school_year_id>/<workshop_id>/cargar",
    "asistance_create",
    assistance.create,
    methods=["POST"],
)

# Admin
app.add_url_rule("/admin", "admin_index", admin.index)
app.add_url_rule("/admin/update", "admin_update", admin.update, methods=["GET", "POST"])

# Home Page
app.add_url_rule("/", "home_page", home.index)


@app.route("/nucleos")
def mapa_osm():
    Configuration.db = get_db()
    configs = Configuration.all()
    Roles.db = get_db()
    user_permissions = Roles.getUserPermissions(
        helper_auth.authenticated(session) or ""
    )
    return render_template(
        "mapa_osm.html", configs=configs, user_permissions=user_permissions
    )
