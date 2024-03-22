#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.orm import declarative_base
Base = declarative_base()
from test import storage
storage.start()


class BaseModel:
    id = Column(String(60), default=str(uuid4()), primary_key=True)
    updated_at = Column(DateTime, default=datetime.utcnow())
    created_at = Column(DateTime, default=datetime.utcnow())




    # def __repr__(self):
    #     return f"[{self.__class__.__name__}] ({self.id}) ({self.__class__.__dict__})"

