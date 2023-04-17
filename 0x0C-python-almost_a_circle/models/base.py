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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A class method that writes JSON string representation to a file

        Args:
            cls: Class Method
            list_objs (list): The list of objects

        Returns:
         The JSON string representation to a file
        """

        file_name = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []

        list_dict = [element.to_dictionary() for element in list_objs]
        json_list = cls.to_json_string(list_dict)
        with open(file_name, "w") as file:
            file.write(json_list)
