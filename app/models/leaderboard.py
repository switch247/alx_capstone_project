# The Leaderboard class represents a table in a database with columns for id, email, quiz_id, score,
# and time.
import uuid
from app import db

class Leaderboard(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    # str conversion for mysql
    email = db.Column(db.String(120), nullable=False)
    quiz_id = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Float, nullable=False)
    time = db.Column(db.Float, nullable=False)
    def __repr__(self):
        return f"Leaderboard(id={self.id}, email={self.email}, quiz_id={self.quiz_id}, score={self.score}, time={self.time})"

    # def __init__(self, email, quiz_id, score, time):
    #     self.email = email
    #     self.quiz_id = quiz_id
    #     self.score = score
    #     self.time = time
