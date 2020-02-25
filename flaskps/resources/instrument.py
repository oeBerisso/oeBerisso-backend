from flask import redirect, render_template, request, url_for, session, abort, flash
from flask_paginate import Pagination
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.instrument import Instrument
from flaskps.models.instrument_type import Instrument_type
from flaskps.helpers import auth as helper_auth
from flaskps.helpers import permissions as helpers_permission
from werkzeug.utils import secure_filename
from flaskps.helpers import form_validation
from flaskps.validations import instrument_new as instrument_validations
from flaskps.validations import instrument_edit as instrument_edit_validations


import random
import os


def new():
    user_permissions = helpers_permission.can_access(["instrument_new"])
    Instrument_type.db = get_db()
    instrument_types = Instrument_type.all()
    configs = config_user()
    return render_template("instrument/new.html", **locals())


def create():
    if helpers_permission.can_access(["instrument_new"]):
        data = request.form.copy()
        data["photo"] = request.files["photo"].filename
        if not form_validation.validate(instrument_validations.rules, data):
            Instrument.db = get_db()
            filename = (
                str(random.getrandbits(128)) + ".jpg"
            )  # hash que se utiliza de nombre para imagen
            f = request.files["photo"]
            f.save(os.path.join("./flaskps/static/uploads", filename))
            data["photo"] = filename
            Instrument.create(data)
            flash("El Instrumento se agrego correctamente", "positive")
            return redirect(url_for("instrument_index"))
        else:
            return redirect(url_for("instrument_new"))


def modify(instrument_id):
    if helpers_permission.can_access(["instrument_update"]):
        if not form_validation.validate(
            instrument_edit_validations.rules, request.form
        ):

            Instrument.db = get_db()

            not_includes_photo = (
                request.files["photo"].filename == ""
            )  # verifico si se envio una imagen
            if not_includes_photo:
                Instrument.update(request.form, instrument_id)
            else:
                data = request.form.copy()
                old_photo = Instrument.get_photo_name(instrument_id)
                os.remove(
                    "./flaskps/static/uploads/" + old_photo
                )  # borro la foto vieja
                filename = (
                    str(random.getrandbits(128)) + ".jpg"
                )  # hash que se utiliza de nombre para imagen
                f = request.files["photo"]
                f.save(os.path.join("./flaskps/static/uploads", filename))
                data["photo"] = filename
                Instrument.update_with_photo(data, instrument_id)
            flash("El instrumento se modifico correctamente.", "positive")
            return redirect(url_for("instrument_index"))
        else:
            return profile(instrument_id)


def config_user():
    Configuration.db = get_db()
    return Configuration.all()


def index():

    user_permissions = helpers_permission.can_access(["instrument_index"])
    Instrument_type.db = get_db()
    instrument_types = Instrument_type.all()
    Instrument.db = get_db()
    if request.args:
        name = request.args.get("name") or ""
        type_id = request.args.get("type_id") or ""
        instruments = Instrument.filter(name, type_id)
    else:
        name = ""
        type_id = ""
        instruments = Instrument.all()

    page = request.args.get("page", type=int, default=1)

    configs = config_user()
    per_page = int(Configuration.get("elementsCount"))
    offset = per_page * (page - 1)
    pagination = Pagination(page=page, per_page=per_page, total=len(instruments))

    instruments = instruments[offset : offset + per_page]

    return render_template("instrument/index.html", **locals())


def delete(id):
    if helpers_permission.can_access(["instrument_destroy"]):
        Instrument.db = get_db()
        old_photo = Instrument.get_photo_name(id)
        os.remove("./flaskps/static/uploads/" + old_photo)  # borro la foto vieja
        Instrument.delete_instrument(id)
        flash("El instrumento a sido eliminado correctamente.", "positive")
        return redirect(url_for("instrument_index"))


def profile(instrument_id):
    user_permissions = helpers_permission.can_access(["instrument_show"])
    configs = config_user()
    Instrument_type.db = get_db()
    instrument_types = Instrument_type.all()
    Instrument.db = get_db()
    instrument = Instrument.show_instrument(instrument_id)
    if instrument is None:
        return redirect(url_for("instrument_index"))
    else:
        Instrument_type.db = get_db()
        Instrument_type.all()
        return render_template("instrument/modify.html", **locals())
