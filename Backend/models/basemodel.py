#!/usr/bin/env python3
""" The base class implementation"""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, Column, DateTime
from sqlalchemy.orm import declarative_base
import models
from helpers.decorators import role_required
Base = declarative_base()
class BaseModel:
    """Base Class"""
    id = Column(String(40), primary_key=True, default=str(uuid4()))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs) -> None:
        """initialize the instance"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id})"
    

    def to_dict(self):
        """returns a dictionary of the instance"""
        newdict = self.__dict__.copy()
        if '_sa_instance_state' in newdict:
            del newdict['_sa_instance_state']
        return newdict


    def save(self):        
        """saves the obj instance"""
        updated_at = datetime.utcnow()
        models.storage.new(self)
        id = models.storage.save(self)
        return id

    def delete(self):
        """deletes the obj"""
        models.storage.delete(self)

    @classmethod
    def get(cls, id):
        """gets the obj from models.storage"""
        obj = models.storage.get(cls, id)
        return obj

    @classmethod
    def all(cls):
        """return all instances of an class"""
        return models.storage.all(cls)
    
    @classmethod
    def count(cls):
        """counts all instances of the class"""
        return models.storage.count(cls)
    
    @classmethod
    @property
    def query(cls):
        """counts all instances of the class"""
        query = models.storage.query(cls)
        return query
