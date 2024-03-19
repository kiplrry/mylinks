#!/usr/bin/env python3
"""Implements the Admin class"""

from sqlalchemy import String, Column
from models.usermodels.user import User

class Admin(User):
    """implements the Admin Class"""
    __tablename__ = 'admins'
    admin_id = Column(String, primary_key=True)
    
    ___mapper_args__ = {
        "polymorphic_identity" : "admins"
    }


