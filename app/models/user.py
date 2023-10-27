import uuid
from app import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    # str conversion for mysql
    username = db.Column('username',db.String(100), nullable=False)
    # phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email}, password={self.password})"

# db.create_all()
# e23275cb-fc71-4a92-8e04-214b9e75bff8