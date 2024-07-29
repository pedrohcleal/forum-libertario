from app.repositories.post_repository import PostRepository

class PostService:
    @staticmethod
    def get_all_posts():
        return PostRepository.get_all()

    @staticmethod
    def get_post_by_id(post_id):
        return PostRepository.get_by_id(post_id)
