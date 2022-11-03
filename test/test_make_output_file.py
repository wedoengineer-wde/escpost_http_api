from . import app, client



def test_print_request(client):
    
    response = client.post("/print")

    assert response.status_code == 200