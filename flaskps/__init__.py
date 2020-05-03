from flask import Flask, flash, request
from flask_session import Session
from flaskps.config import Config
from flaskps.decorators.auth import login_required
from flaskps.resources import auth
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from oauthlib.oauth2 import WebApplicationClient

app = Flask(__name__)

app.secret_key = Config.GOOGLE_CLIENT_SECRET
# OAuth 2 client setup
client = WebApplicationClient(Config.GOOGLE_CLIENT_ID)


# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'sdlkjhghsgfinjpjaSOJIdSFOJSAdKJFA1'
app.config.from_object(Config)
jwt = JWTManager(app)


app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/glogin")
def glogin():
    return auth.google_login(client)

@app.route("/api/v1.0/auth", methods=["POST"])
def login():
    return auth.login(request, create_access_token)

@app.route("/api/v1.0/")
@login_required
def home():
    return "hello word"