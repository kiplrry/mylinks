#!/usr/bin/python3

from test.base import Base, BaseModel
from sqlalchemy import Column, String, Integer

class User(BaseModel, Base):

    __tablename__ = 'emps'

    name = Column(String(20), nullable=True)
    age = Column(Integer)
    print('user class created ')
    def __init__(self, name, age):
        self.name = name
        self.age = age