from flask import Flask, flash, request
from flask_session import Session
from flaskps.config import Config
from flaskps.decorators.auth import login_required
from flaskps.resources import auth
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'sdlkjhghsgfinjpjaSOJIdSFOJSAdKJFA1'
app.config.from_object(Config)
jwt = JWTManager(app)


app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/api/v1.0/auth", methods=["POST"])
def login():
    return auth.login(request, create_access_token)

@app.route("/api/v1.0/")
@login_required
def home():
    return "hello word"