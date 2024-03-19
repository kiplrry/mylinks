#!/usr/bin/env python3
"""Implement the DB storage"""

from sqlalchemy import create_engine
from models.basemodel import Base


class Storage():
    """The Storage Class"""
    
    __engine = None
    __session = None

    def __init__(self) -> None:
        """initializing the class"""
        USER = None
        PASS = None
        HOST = None
        DB = None
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER, PASS, HOST, DB)
                                      )
    
    def save(self, obj):
        """Saves the obj to storage"""
        pass

    def new(self, obj):
        """Saves obj to session"""
        pass
    
    def all(self, cls):
        """query on the current database session"""
        pass
    
    def reload(self):
        """reloads the session"""
        pass

    def delete(self, obj):
        """deletes the obj in storage"""
        pass

    def get(self, cls, id):
        """gets an object"""

    def close(self):
        """close the session"""

    def count(self, cls):
        """Count obj in DB"""
