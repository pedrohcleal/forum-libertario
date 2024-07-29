from app.models import db, User

class UserRepository:
    @staticmethod
    def get_all():
        return [user.username for user in User.query.all()]

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id).username
