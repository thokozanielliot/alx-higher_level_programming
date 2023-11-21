#!/usr/bin/python3
"""
conatins State classs & Base, an instance of declarative_base()
"""
from sqlalchemy import COlumn, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

myMetaData = MetaData()
Base = declarative_base(metadata=myMetaData)


class State(Base):
    """
    Class with id & name attributes of each state
    """
    __tableName__ = "states"
    id = Column(Integer, unique=True, nullaable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")

