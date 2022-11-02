from venv import create
from config import Config
from app import create_app

config = Config("settings.json")

app = create_app(config)


if __name__ == "__main__":

    app.run(host=config.SERVER_NAME, port=config.SERVER_PORT, debug=True)
