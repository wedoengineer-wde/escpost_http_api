from flask import Flask

from config import Config


def create_app(config: Config) -> Flask:
    """ A function used to create all the general flask configurations

    Args:
        config (Config): It recieves the Config file

    Returns:
        Flask: The app configured
    """
    app = Flask(__name__)

    app.config.from_mapping(config.flask_settings)

    @app.route("/is_up")
    def hello_world():
        return "OK"

    return app
