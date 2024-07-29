import pytest
from app import create_app
from app.extensions import db
from app.models import Post

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados para os testes

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()  # Remove todas as tabelas após os testes

def test_get_posts(client):
    # Adiciona um post fictício para teste
    with client.application.app_context():
        post = Post(title='Test Post', content='Content of the test post.')
        db.session.add(post)
        db.session.commit()

    response = client.get('/posts/')
    assert response.status_code == 200
    assert b'Test Post' in response.data
