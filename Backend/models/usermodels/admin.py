#!/usr/bin/env python3
"""Implements the Admin class"""

from uuid import uuid4
from sqlalchemy import String, Column, ForeignKey
from models.usermodels.user import User

class Admin(User):
    """implements the Admin Class"""
    __tablename__ = 'admin'
    user_id = Column(String(60), ForeignKey('user.id'))
    admin_id = Column(String(60), primary_key=True)
    
    __mapper_args__ = {
        "polymorphic_identity" : "admin"
    }
    def __init__(self, name, age, username) -> None:
        self.admin_id = str(uuid4())
        super().__init__(name, age, username)