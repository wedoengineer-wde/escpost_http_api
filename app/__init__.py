from flask import Flask

from config import Config


def create_app(config: Config):
    app = Flask(__name__)

    app.config.from_mapping(config.flask_settings)

    @app.route("/is_up")
    def hello_world():
        return "OK"

    return app
