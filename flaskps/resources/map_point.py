from flask import jsonify
from flaskps.db import get_db
from flaskps.models.map_points import MapPoints


def index():
    MapPoints.db = get_db()
    locations = MapPoints.all()

    return jsonify(locations=locations)
