from app.models import db, Post

class PostRepository:
    @staticmethod
    def get_all():
        return [{'title': post.title, 'content': post.content} for post in Post.query.all()]

    @staticmethod
    def get_by_id(post_id):
        post = Post.query.get(post_id)
        return {'title': post.title, 'content': post.content}
