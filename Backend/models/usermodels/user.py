#!/usr/bin/python3
"""implements the user class"""

from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, Integer



class User(BaseModel, Base):
    """ The User Class"""

    __tablename__ = "users"

    id = Column(String(20), primary_key=True)
    name = Column(String(20), default='anonymous')
    email = Column(String(30))
    username = Column(String, unique=True)

    ___mapper_args__ = {
        "polymorphic_identity": "User",
        "polymorphic_on": "type",
    }


    def __repr__(self) -> str:
        """String representation of the obj"""
        pass
