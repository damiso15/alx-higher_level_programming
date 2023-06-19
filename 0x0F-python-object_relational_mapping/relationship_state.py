#!/usr/bin/python3
"""
A Relationship State model that links a table in datase.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    A class State that inherits from Base and links to MySQL table
    Class Attribute
        id (int): represents a column of an auto-generated, unique integer,
                  can't be null and is a primary key
        name (str): represents a column of a string with maximum 128
                    characters and can't be null
        cities (str): represent a relationship with the class City. If the
                      State object is deleted, all linked City objects must
                      be automatically deleted. Also, the reference from a City
                      object to his State should be named state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
