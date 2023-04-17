#!/usr/bin/python3
"""
A first class Base
"""
import json
from os import path


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

    @staticmethod
    def from_json_string(json_string):
        """
        A static method that returns the list of the JSON string representation

        Args:
            json_string (dict): A list of dictionaries

        Return:
            The list of the JSON string representation
        """

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        A class method that returns an instance with all attributes already set

        Args:
            cls: Class Method
            dictionary (dict): A double pointer to a dictionary

        Return:
            An instance with all attributes already set
        """

        if cls.__name__ == "Rectangle":
            created = cls(1, 1)
        elif cls.__name__ == "Square":
            created = cls(1)

        created.update(**dictionary)
        return created

    @classmethod
    def load_from_file(cls):
        """
        A class method that returns a list of instances

        Args:
            cls: Class MEthod

        Return:
            A list of instances
        """

        file_name = "{}.json".format(cls.__name__)
        instance_list = []

        if not path.isfile(file_name):
            return instance_list

        with open(file_name, "r") as f:
            json_str = f.read()

        json_list = cls.from_json_string(json_str)
        for item in json_list:
            instance_list.append(cls.create(**item))

        return instance_list
