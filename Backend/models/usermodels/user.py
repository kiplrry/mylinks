#!/usr/bin/python3
"""implements the user class"""
from flask_login import UserMixin
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from helpers.decorators import role_required

class User(BaseModel, UserMixin, Base):
    """ The User Class"""
    __tablename__ = "user"
    name = Column(String(20), default='anonymous')
    gender = Column(String(1), default='M')
    email = Column(String(30), nullable=True)
    username = Column(String(20), unique=True, nullable=True)
    password = Column(String(60), default='123456')
    role = Column(String(20), default='user')
    links = relationship('Link', back_populates='user')

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": 'role'
    }

    def __init__(self, *args, **kwargs) -> None:
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.username  = kwargs['username']
        super().__init__()
    

        