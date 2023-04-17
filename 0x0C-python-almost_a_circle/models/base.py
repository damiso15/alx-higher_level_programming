#!/usr/bin/python3
"""
A first class Base
"""
import json


class Base:
    """
    A first class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        A class constructor

        Attributes:
            id (int): the id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        A static method that returns the JSON string representation

        Args:
            list_dictionaries (dict): The dictionary to convert to JSON

        Returns:
            The returns the JSON string representation
        """

        json_obj = json.dumps(list_dictionaries)
        return json_obj
