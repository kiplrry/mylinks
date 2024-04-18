#!/usr/bin/env python3
"""Implement the DB storage"""

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.basemodel import Base
from sqlalchemy.exc import IntegrityError, OperationalError


config = dotenv_values('.env')
class Storage():
    """The Storage Class"""
    
    __engine = None
    __session = None

    def __init__(self) -> None:
        """initializing the class"""
        USER = config['USER']
        PASS = config['PASS']
        HOST = config['HOST']
        DB = config['DB']
        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(USER, PASS, HOST, DB)
                                        )
        except OperationalError as err:
            print(f'err occured {err}')
    
    def save(self, obj):
        """Saves the obj to storage"""
        try:
            self.__session.commit()
            return obj.id
        except IntegrityError as err:
            print(f'{obj.__class__.__name__} not created, duplicate')
            return None
        
        return None

    def new(self, obj):
        """Saves obj to session"""
        self.__session.add(obj)
    
    def all(self, cls):
        """query on the current database session"""
        vals = self.__session.query(cls).all()
        return vals
    
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
    
    def query(self, cls):
        """Return query"""
        return self.__session.query(cls)

