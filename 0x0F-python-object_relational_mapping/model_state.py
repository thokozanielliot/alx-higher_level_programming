#!/usr/bin/python3
"""
Conatins State class & Base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)


class State(Base):
    """
    Class with id & name attributes of each state
    """
    __tableName__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

