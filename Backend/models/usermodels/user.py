#!/usr/bin/python3
"""implements the user class"""


from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    """ The User Class"""
    __tablename__ = "user"
    name = Column(String(20), default='anonymous')
    gender = Column(String(1), default='M')
    email = Column(String(30), nullable=True)
    username = Column(String(20), unique=True, nullable=True)
    role = Column(String(20))

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": 'role'
    }
    def __init__(self, name, age, username) -> None:
        self.name = name
        self.age = age
        self.username  = username
        super().__init__()