from flask import Blueprint, jsonify


app = Blueprint('action', __name__)

@app.route("/api1")
def api1():
    ret = {"hoge": 1, "piyo":2, "c": ["a","b"]}
    return jsonify(ret)