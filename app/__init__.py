from flask import Flask
from app.extensions import db
from app.routes.user_routes import user_bp
from app.routes.post_routes import post_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(post_bp, url_prefix='/posts')

    return app
