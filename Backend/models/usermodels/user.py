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
        # self.name = kwargs['name']
        # self.age = kwargs['age']
        # self.username  = kwargs['username']
        if kwargs:
            for arg, val in kwargs.items():
                setattr(self, arg, val)

        super().__init__()
    
    def get_links(self):
        """get a list of user links"""
        links = self.links
        link_list = []
        for link in links:
            link_list.append(link.to_dict())

        return link_list
    
    @classmethod
    def get(cls, id_or_username):
            user = super().get(id=id_or_username) or \
                    super().query.filter_by(username=id_or_username).first()

            print(f'>>> {user}')
            return user

    @classmethod
    def get_admins(cls):
        pass
    

        