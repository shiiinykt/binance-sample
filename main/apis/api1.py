from flask import Blueprint

app = Blueprint('action', __name__)

@app.route("/api1")
def api1():
    return "{api1}"