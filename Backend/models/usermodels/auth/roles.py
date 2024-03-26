from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from models.basemodel import Base

class Role(Base):
    """the base role"""

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True)
    permissions = relationship('Permission', back_populates='permissions')
    

    def __init__(self, name):
        self.role_name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.getter
    def name(self, name):
        self.__name = name
    
