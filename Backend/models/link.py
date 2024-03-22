#!/usr/bin/env python3
"""implementing the link class"""

from uuid import uuid4
from sqlalchemy import Column, String
from models.basemodel import Base, BaseModel

class Link(BaseModel, Base):
    """Class Link"""
    
    __tablename__ = 'links'

    name = Column(String(20))
    url = Column(String)
    descr = Column(String)

    

    