#!/usr/bin/python3
"""
A State model that links a table in datase.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of Base
Base = declarative_base()


class State(Base):
    """
    A class State that inherits from Base and links to MySQL table
    Class Attribute
        id (int): represents a column of an auto-generated, unique integer,
                  can't be null and is a primary key
        name (str): represents a column of a string with maximum 128
                    characters and can't be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
