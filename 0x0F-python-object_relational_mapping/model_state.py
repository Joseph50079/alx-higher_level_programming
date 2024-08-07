#!/usr/bin/python3

"""This module is for ORM sqlalchemy use"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from model_city import City

mymetadata = MetaData()

Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Creates State base my Mysql database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
#    cities = relationship("City", back_populates='states')
