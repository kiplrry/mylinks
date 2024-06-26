#!/usr/bin/env python3
"""implementing the link class"""

from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.basemodel import Base, BaseModel

class Link(BaseModel, Base):
    """Class Link"""
    
    __tablename__ = 'links'

    name = Column(String(20))
    url = Column(Text)
    descr = Column(Text)
    user_id = Column(String(60), ForeignKey('user.id'))
    user = relationship('User', back_populates='links')

    def __init__(self, *args, **kwargs) -> None:
        #TODO : ensure url, descr, user_id and name
        if kwargs:
            # self.name = kwargs.get('name')
            # self.url = kwargs.get('url')
            # self.descr = kwargs.get('descr')
            for arg, val in kwargs.items():
                setattr(self, arg, val)
        super().__init__()
    
    # @property
    # def name(self):
    #     """get the name"""
    #     return self.__name
    
    # @name.setter
    # def name(self, name: str):
    #     """set name"""
    #     # if not ensure_type(name, str):
    #     #     return
    #     self.__name = name
    
    # @property
    # def url(self):
    #     """get url"""
    #     return self.__url
    
    # @url.setter
    # def url(self, url):
    #     """set url"""
    #     # if not valid_url(url):
    #     #     return
        
    #     self.__url = url
    
    # @property
    # def descr(self):
    #     """get description"""
    #     return self.__descr
    
    # @descr.setter
    # def descr(self, descr):
    #     """set description"""
    #     if not ensure_type(descr, str):
    #         return
    #     self.__descr = descr
    
    def save(self):
        """saves the link"""
        if not self.user_id:
            print('must have a user id')
            return
        return super().save()

    

