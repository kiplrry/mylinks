#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.orm import declarative_base
Base = declarative_base()



class User(Base):

    __tablename__ = 'users'

    id = Column(String(80), default=str(uuid4()), primary_key=True)
    name = Column(String(20), nullable=True)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow())

    # def __repr__(self):
    #     return f"[{self.__class__.__name__}] ({self.id}) ({self.__class__.__dict__})"

