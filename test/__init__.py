from main import create_dependencies
from main import create_routes
from config import Config
import pytest
import os
import shutil


def tmp_config():
    return Config("./test/resources/test_settings.json")


def delete_temp_folder():
    config = tmp_config()
    if os.path.exists(config.output_folder):
        shutil.rmtree(config.output_folder)


@pytest.fixture(scope="session")
def app():
    config = tmp_config()
    delete_temp_folder()
    app, printer, logger = create_dependencies(config)

    app = create_routes(app, printer, logger)
    # other setup can go here
    yield app
    delete_temp_folder()
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
