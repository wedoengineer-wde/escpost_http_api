
from config import Config

"""
{
    'hostname' : 'localhost' , 
    'port' : '5620' , 
    'printer_driver' : 'Dummy' , 
    'printer_settings' : {
    },
    "output_folder" : "output",
    "output_file_format" : "%Y-%m-%d %H-%M-%s.txt"
}
"""


def test_reading_settings():
    test_json_settings = "./test_settings.json"

    config = Config(test_json_settings)

    assert config.SERVER_NAME == 'localhost'
