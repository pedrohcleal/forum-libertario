from app import create_app
from app.extensions import db
from app.models import User, Post

def add_fixtures():
    app = create_app()
    
    with app.app_context():
        # Adiciona usuários fictícios
        user1 = User(username='john_doe', email='john.doe@example.com')
        user2 = User(username='jane_smith', email='jane.smith@example.com')

        db.session.add(user1)
        db.session.add(user2)

        # Adiciona posts fictícios
        post1 = Post(title='First Post', content='This is the content of the first post.')
        post2 = Post(title='Second Post', content='This is the content of the second post.')

        db.session.add(post1)
        db.session.add(post2)

        # Commit as mudanças no banco de dados
        db.session.commit()
        print("Dados fictícios adicionados com sucesso!")

if __name__ == '__main__':
    add_fixtures()
