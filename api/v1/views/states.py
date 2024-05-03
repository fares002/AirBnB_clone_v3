#!/usr/bin/python3
"""
handle State objects
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    """get all states"""
    states = storage.all(State).values()
    states = [state.to_dict() for state in states]
    return states, 200


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state(state_id):
    """get a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict(), 200


@app_views.route("/states/<state_id>", methods=["DELETE"])
def delete_state(state_id):
    """delete a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    for city in state.cities:
        storage.delete(city)

    storage.delete(state)
    storage.save()

    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """create a state"""
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**data)
    storage.new(state)
    storage.save()
    return state.to_dict(), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """update a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()
    return state.to_dict(), 200
