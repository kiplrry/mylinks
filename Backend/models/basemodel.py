#!/usr/bin/env python3
""" The base class implementation"""

from datetime import datetime
# from uuid import uuid4
from sqlalchemy import String, Column, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel:
    """Base Class"""

    id = Column(String(20), primary_key=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self) -> None:
        """initialize the instance"""

    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id})"
    
    def to_dict(self):
        """returns a dictionary of the instance"""
        pass

    def save(self):        
        """saves the obj instance"""
        pass

    def delete(self):
        """deletes the obj"""
        pass

    def all(self):
        """return all instances of an class"""
        pass
