from app.models.BaseModel import *
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

class User (UserMixin,BaseModel):
    __tablename__ = 'users'
    # user-specific fields here
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    name = Column(String(255))

