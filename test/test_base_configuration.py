
from . import app, client


def test_request_example(client):
    response = client.get("/is_up")
    assert b"OK" in response.data
    assert response.status_code == 200
