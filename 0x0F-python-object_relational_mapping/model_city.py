#!/usr/bin/python3
"""
A City model that links a table in dataset
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    A class City that inherits from Base and links to MySQL table
    Class Attribute
        id (int): represents a column of an auto-generated, unique integer,
                  can't be null and is a primary key
        name (str): represents a column of a string with maximum 128
                    characters and can't be null
        state_id (int): represents a column of an inteher, can't be null and
                        is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
