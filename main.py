from config import Config
from app import create_app
from printer_controller import create_printer


def create_routes(app, printer):

    @app.route("/is_up")
    def hello_world():
        return "OK"

    @app.route("/print", methods=["POST"])
    def print():

        printer.text("hola")

        return "ok"

    return app


if __name__ == "__main__":

    config = Config("settings.json")

    app = create_app(config)

    printer = create_printer(config.printer_driver, config.printer_settings)

    app = create_routes(app, printer)

    app.run(host=config.SERVER_NAME, port=config.SERVER_PORT, debug=True)
