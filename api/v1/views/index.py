#!/usr/bin/python3
"""
api/v1/views/status API endpoints
"""

from flask import jsonify, make_response
from api.v1.views import app_views

from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    status
    """
    data = {
        "status": "OK"
    }

    resp = jsonify(data)
    resp.status_code = 200

    return make_response(resp)


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    Return the number of each object 
    in the database
    """
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }

    resp = jsonify(data)
    resp.status_code = 200

    return make_response(resp)
