#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer,
                        PrimaryKeyConstraint, UniqueConstraint, Index)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dog(Base):

    __tablename__ = 'dogs'
 

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def __repr__(self):
        return f"<Dog name is {self.name},and dog breed is :{self.breed}>"
