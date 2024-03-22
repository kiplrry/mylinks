#!/usr/bin/env python3
""" The base class implementation"""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, Column, DateTime
from sqlalchemy.orm import declarative_base
import models
Base = declarative_base()
class BaseModel:
    """Base Class"""
    id = Column(String(40), primary_key=True, default=str(uuid4()))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self) -> None:
        """initialize the instance"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id})"
    
    def to_dict(self):
        """returns a dictionary of the instance"""
        return self.__dict__

    def save(self):        
        """saves the obj instance"""
        updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save(self)

    def delete(self):
        """deletes the obj"""
        models.storage.delete(self)

    def get(self):
        """gets the obj from models.storage"""
        # models.storage.get(self)

    @classmethod
    def all(cls):
        """return all instances of an class"""
        models.storage.all(cls)
    
    @classmethod
    def count(cls):
        """counts all instances of the class"""
        return models.storage.count(cls)
