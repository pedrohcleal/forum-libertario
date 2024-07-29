import pytest
from app import create_app
from app.extensions import db
from app.models import User

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

def test_get_users(client):
    # Adiciona um usuário fictício para teste
    with client.application.app_context():
        user = User(username='test_user', email='test_user@example.com')
        db.session.add(user)
        db.session.commit()

    response = client.get('/users/')
    assert response.status_code == 200
    assert b'test_user' in response.data
