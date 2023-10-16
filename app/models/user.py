import uuid
from app import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    # str conversion for mysql
    username = db.Column('username',db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False, unique=True)
    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, phone_number={self.phone_number}, email={self.email}, password={self.password})"

# db.create_all()