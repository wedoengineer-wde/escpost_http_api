from . import app, client, tmp_config
import os


def read_file(file):
    f = open(file, "r")
    return f.read()


def test_print_request(client):

    config = tmp_config()
    output_folder = config.output_folder
    file_format = config.output_file_format
    data = {
        "text": "Text to print"
    }
    response = client.post("/print", json=data)

    assert response.status_code == 200

    assert os.path.exists(output_folder)

    dirs = os.listdir(output_folder)
    assert len(dirs) == 1

    file_name = dirs[0]
    assert file_name.split(".")[-1] == file_format.split(".")[-1]

    file_path = os.path.join(output_folder, file_name)
    text = read_file(file_path)

    assert "Text to print" in text

    # Other post

    data2 = {
        "text": "Another text"
    }
    response = client.post("/print", json=data2)

    assert response.status_code == 200

    text2 = read_file(file_path)
    assert "Another text" in text2
