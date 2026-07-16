from flask import Blueprint, jsonify

from api.services import (
    get_prices,
    get_change_points,
    get_events,
    get_event_matches
)

api = Blueprint("api", __name__)
@api.route("/prices", methods=["GET"])
def prices():

    return jsonify(
        get_prices()
    )
@api.route("/change-points", methods=["GET"])
def change_points():

    return jsonify(
        get_change_points()
    )
@api.route("/events", methods=["GET"])
def events():

    return jsonify(
        get_events()
    )

@api.route("/event-correlation", methods=["GET"])
def event_correlation():

    return jsonify(
        get_event_matches()
    )