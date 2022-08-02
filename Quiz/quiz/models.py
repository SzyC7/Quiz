from quiz import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    total = db.Column(db.Integer)
    scores = db.relationship("Score", backref="user", lazy="dynamic")

    is_admin = db.Column(db.Boolean, default=False)

    def get(self, username):
        return self.id


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), index=True, nullable=True)
    question = db.Column(db.String(20), index=True, nullable=True)
    level = db.Column(db.String(20), index=True, nullable=True)
    score = db.Column(db.Integer, index=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, category, question, level, score, user_id):
        self.category = category
        self.question = question
        self.level = level
        self.score = score
        self.user_id = user_id