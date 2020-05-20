from flask import jsonify
from flaskps.db import get_db
from flaskps.models.configuration import Configuration

def index():

    Configuration.db = get_db()
    config = Configuration.get_footer_data()

    return jsonify(
      {
        "maintenance": config["maintenance"],
        "email": config["email"],
      }
    )