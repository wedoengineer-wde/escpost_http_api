from flask import Flask

from config import Config
app = Flask(__name__)

config = Config("settings.json")
app.config.from_mapping(config.flask_settings)


@app.route("/is_up")
def hello_world():
    return "OK"
