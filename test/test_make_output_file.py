from . import app, client, tmp_config
import os


def test_print_request(client):
    
    config = tmp_config()
    output_folder = config.output_folder

    response = client.post("/print")

    assert response.status_code == 200

    assert os.path.exists(output_folder)
