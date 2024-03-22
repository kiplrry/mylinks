#!/usr/bin/env python3
"""Implement the DB storage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.basemodel import Base

class Storage():
    """The Storage Class"""
    
    __engine = None
    __session = None

    def __init__(self) -> None:
        """initializing the class"""
        USER = 'larry'
        PASS = 'pass'
        HOST = 'localhost'
        DB = 'flasktest'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER, PASS, HOST, DB)
                                      )
    
    def save(self, obj):
        """Saves the obj to storage"""
        self.__session.commit()

    def new(self, obj):
        """Saves obj to session"""
        self.__session.add(obj)
    
    def all(self, cls):
        """query on the current database session"""
        pass
    
    def reload(self):
        """reloads the session"""
        Base.metadata.create_all(bind=self.__engine)
        print('reloaded')
        print(Base.metadata.tables.keys())
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped = scoped_session(sess)
        self.__session = scoped


    def delete(self, obj):
        """deletes the obj in storage"""
        if obj:
            self.__session.delete(obj)

    def get(self, cls, id):
        """gets an object"""
        if cls and id:
            obj = self.__session.query(cls).filter_by(id=id).first()
            return obj
        return None

    def close(self):
        """close the session"""
        self.__session.remove()

    def count(self, cls):
        """Count obj in DB"""
        count = self.__session.query(cls).count()
        return count

