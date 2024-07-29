from flask import Blueprint, jsonify, request
from app.services.post_service import PostService

post_bp = Blueprint('posts', __name__)

@post_bp.route('/', methods=['GET'])
def get_posts():
    posts = PostService.get_all_posts()
    return jsonify(posts)

@post_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = PostService.get_post_by_id(post_id)
    return jsonify(post)
