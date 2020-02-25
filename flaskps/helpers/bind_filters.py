from flaskps.models.school import School
from flaskps.models.level import Level
from flaskps.models.gender import Gender
from flaskps.models.town_down import TownDown
from flaskps.models.instrument_type import Instrument_type
from flaskps.models.reference_api import ReferenceApi

from flaskps.db import get_db


def bind_template_filters(app):
    @app.template_filter("translate_bool")
    def human_boolean(bool):
        return "Si" if int(bool) else "No"

    @app.template_filter("translate_checked")
    def checked(bool):
        return "checked" if int(bool) else ""

    @app.template_filter("translate_school")
    def school_name(id):
        School.db = get_db()
        return School.find_school_name(id)[0]["name"]

    @app.template_filter("translate_level")
    def level_name(id):
        Level.db = get_db()
        return Level.find_level_name(id)[0]["name"]

    @app.template_filter("translate_gender")
    def gender_name(id):
        Gender.db = get_db()
        return Gender.find_gender_name(id)[0]["name"]

    @app.template_filter("translate_town_down")
    def town_down_name(id):
        TownDown.db = get_db()
        return TownDown.find_town_down_name(id)[0]["name"]

    @app.template_filter("translate_document_type")
    def document_type_name(id):
        ReferenceApi.db = get_db()
        return ReferenceApi.find_document_type_name(id)

    @app.template_filter("translate_location")
    def location_name(id):
        ReferenceApi.db = get_db()
        return ReferenceApi.find_location_name(id)

    @app.template_filter("translate_instrument_type")
    def instrument_type_name(id):
        Instrument_type.db = get_db()
        return Instrument_type.find_instrument_type_name(id)[0]["name"]
