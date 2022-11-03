from config import Config
from app import create_app
from printer_controller import create_printer
import os

from datetime import datetime
class Logger():
    
    def __init__(self , output_folder:str , output_format:str ) :
        self.output_folder = output_folder
        self.output_format = output_format 
        
    def _get_file_path(self) -> str:
        file_name = datetime.now().strftime ( self.output_format ) 
        return os.path.join(self.output_folder , file_name)
        
    def print_to_file(self, output : str ) -> bool:
        file_path = self._get_file_path()

        f = open(file_path, "wb")
        f.write(output)
        f.close()


def create_routes(app  , printer  , logger : Logger):

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

    app = create_app(config)

    printer = create_printer(config.printer_driver, config.printer_settings)
    
    logger = Logger( output_folder= config.output_folder , output_format=config.output_file_format ) 
    
    app = create_routes(app, printer , logger)

    app.run(host=config.SERVER_NAME, port=config.SERVER_PORT, debug=True)
