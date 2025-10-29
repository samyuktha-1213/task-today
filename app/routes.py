from flask import Blueprint, jsonify

main_routes = Blueprint("main", __name__)

@main_routes.route("/")
def home():
    return jsonify({"message": "Hello from Flask App!"}), 200

