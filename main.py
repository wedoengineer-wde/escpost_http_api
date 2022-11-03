from config import Config
from app import create_app
from logger import Logger

from printer_controller import create_printer

def create_dependencies(config : Config) : 
    app = create_app(config)

    printer = create_printer(config.printer_driver, config.printer_settings)

    logger = Logger(output_folder=config.output_folder,
                    output_format=config.output_file_format)
    
    return app , printer , logger

def create_routes(app, printer, logger: Logger):

    @app.route("/is_up")
    def hello_world():
        return "OK"

    @app.route("/print", methods=["POST"])
    def print():

        printer.text("hola")

        logger.print_to_file(printer.output)
        return "ok"

    return app


if __name__ == "__main__":

    config = Config("settings.json")

    app , printer , logger = create_dependencies ( config)

    app = create_routes(app, printer, logger)

    app.run(host=config.SERVER_NAME, port=config.SERVER_PORT, debug=True)
