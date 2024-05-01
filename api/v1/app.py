#!/usr/bin/python3
"""
app filestorage
"""

from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage


app = Flask(__name__)

CORS(app, resources={r'api/v1/*': {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown(exception):
    """
    close storage"""
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """
    handles error 404"""
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    return resp, 404


if __name__ == "__main__":
    HOST  = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
