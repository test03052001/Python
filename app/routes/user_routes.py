from flask import Blueprint, request, jsonify
from app.services import user_service

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_service.register_user(data)
    return jsonify({"message": "User created"})

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = user_service.list_users()
    return jsonify(users)