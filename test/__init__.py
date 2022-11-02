

from app import create_app
from printer_controller import create_printer
from main import create_routes
from config import Config
import pytest

def tmp_config():
    return Config("./test/resources/test_settings.json")

@pytest.fixture(scope="session")
def app():
    config = tmp_config()
    app = create_app(config)
    printer = create_printer(config.printer_driver , config.printer_settings)
    app = create_routes(app , printer )
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def ctx(app):
    with app.app_context() as ctx:
        yield ctx

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
