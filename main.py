from config import Config
from app import create_app, request
from logger import Logger

from printer_controller import create_printer


def create_dependencies(config: Config):
    app = create_app(config)

    printer = create_printer(config.printer_driver, config.printer_settings)

    logger = Logger(output_folder=config.output_folder,
                    output_format=config.output_file_format)

    return app, printer, logger


def create_routes(app, printer, logger: Logger):

    @app.route("/is_up")
    def hello_world():
        return "OK"

    @app.route("/open_cashdraw", methods=["POST"])
    def open_cashdraw():
        printer.cashdraw(config.cashdrawer_pin)
        if printer.__class__.__name__ == "Dummy":
            logger.print_to_file(printer.output)
        return {'ok': 'ok'}

    @app.route("/print", methods=["POST"])
    def to_print():

        data = request.get_json()
        text = data["text"]

        print(text)
        printer.text(text)
        printer.cashdraw(config.cashdrawer_pin)
        if printer.__class__.__name__ == "Dummy":
            logger.print_to_file(printer.output)
        response = {'ok': 'ok'}
        return response

    @app.route("/cut", methods=["POST"])
    def to_cut():
        # printer.text("\n")
        printer.cut()
        printer.open

        if printer.__class__.__name__ == "Dummy":
            logger.print_to_file(printer.output)
        return {'ok': 'ok'}

    return app


if __name__ == "__main__":

    config = Config("settings.json")

    app, printer, logger = create_dependencies(config)

    app = create_routes(app, printer, logger)

    app.run(host=config.SERVER_NAME, port=config.SERVER_PORT, debug=True)
