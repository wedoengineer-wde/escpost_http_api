import os
import json
from collections import OrderedDict


def open_json(file: str) -> dict:
    with open(file, 'r') as config_file:
        data = config_file.read()
    return json.loads(data, object_pairs_hook=OrderedDict)


class Config():

    def __init__(self, json_file="settings.json"):

        if not os.path.exists(json_file):
            raise "File {0} does not exist".format(json_file)

        settings = open_json(json_file)

        Config.SERVER_NAME = settings.get("hostname", "localhost")
        Config.SERVER_PORT = settings.get("port", "5620")
        Config.flask_settings = settings["flask_settings"]
        Config.printer_driver = settings["printer_driver"]
        Config.printer_settings = settings["printer_settings"]
        Config.output_folder = settings["output_folder"]
        Config.output_file_format = settings["output_file_format"]
