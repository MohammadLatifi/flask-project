from main import BaseModel
from sqlalchemy import Column, Integer, String

class User (BaseModel):
    __tablename__ = 'users'
    # user-specific fields here
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))

