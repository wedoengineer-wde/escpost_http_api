

from main import app as application
import pytest


@pytest.fixture()
def app():
    app = application
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
