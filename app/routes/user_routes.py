from flask import Blueprint, Response, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def get_users() -> Response:
    users = UserService.get_all_users()
    return jsonify(users)

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id) -> Response:
    user = UserService.get_user_by_id(user_id)
    return jsonify(user)
