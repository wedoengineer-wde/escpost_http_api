
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

    config = Config("./test/resources/test_settings.json")
    assert config.SERVER_NAME == 'localhost'

    config2 = Config("./test/resources/test_settings_2.json")
    assert config2.SERVER_NAME == "0.0.0.0"


def test_all_the_variables_are_loaded():

    config = Config("./test/resources/test_settings.json")

    assert config.SERVER_NAME == 'localhost'
    assert config.SERVER_PORT == "5620"
    assert config.printer_driver == "Dummy"
    assert type(config.printer_settings).__name__ == "OrderedDict"
    assert config.output_folder == "test_output"
    assert config.output_file_format == "%Y-%m-%d %H-%M-%s.txt"
