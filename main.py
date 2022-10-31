from flask import Flask


app = Flask(__name__)

@app.route("/is_up")
def hello_world():
    return "OK"
