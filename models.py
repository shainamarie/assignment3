from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

from app import app

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, first_name='', last_name='', gender='', email='', password=''):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.password = password






db.create_all()