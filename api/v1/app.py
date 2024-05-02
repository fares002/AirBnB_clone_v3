#!/usr/bin/python3
"""
Start Flask application
"""

from flask import Flask, jsonify, Blueprint, make_response
from flask_cors import CORS
from os import getenv
from api.v1.views import app_views
from models import storage


app = Flask(__name__)

cors = CORS(app, resources={r'api/v1/*': {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    close"""
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """
    error"""
    data = {
        "error": "Not found"
        }
    resp = make_response(jsonify(data))
    return resp, 404


if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
