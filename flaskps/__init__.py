from flask import Flask, flash, request, url_for, jsonify
from flask_session import Session
from flaskps.config import Config
from flaskps.decorators.auth import login_required
from flaskps.resources import auth
from flask_cors import CORS

from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
from oauthlib.oauth2 import WebApplicationClient

app = Flask(__name__)

app.secret_key = Config.GOOGLE_CLIENT_SECRET
# OAuth 2 client setup
client = WebApplicationClient(Config.GOOGLE_CLIENT_ID)

CORS(app, resources={r"/api/*": {"origins": "*"}})
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "sdlkjhghsgfinjpjaSOJIdSFOJSAdKJFA1"
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(Config)
jwt = JWTManager(app)


app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/glogin")
def glogin():
    return auth.google_login(client)

# routes
app.add_url_rule("/api/v1.0/register", "user_create", auth.create, methods=["POST"])


@app.route("/api/v1.0/auth", methods=["POST"])
def login():
    return auth.login(request, create_access_token)


@app.route("/api/v1.0/")
@login_required
def home():
    return "hello word"

@app.route("/")
def test():
    return "<h1>hello world</h1>"


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/routes")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return jsonify({"url": links})