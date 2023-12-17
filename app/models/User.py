from extensions import db
from flask_login import UserMixin

class User (UserMixin,db.Model):
    __tablename__ = 'users'
    # user-specific fields here
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))

