from app.models import User
from app.extensions import db, app

user1 = User(
    username='admin',
    password='admin',
    email = 'adminmail@gmail.com'
)

user2 = User(
    username = 'admin2',
    password = 'admin2',
    email = 'admin2mail@gmail.com'
)

with app.app_context():
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()