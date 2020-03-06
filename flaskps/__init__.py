from flask import Flask
from flask_session import Session
from flaskps.config import Config


app = Flask(__name__)
app.config.from_object(Config)

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return "hello word"