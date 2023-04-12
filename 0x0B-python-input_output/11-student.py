#!/usr/bin/python3
"""
A class Student
"""


class Student:
    """
    A class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age

        Attributes:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A public method that retrieves a dictionary representation of a
        Student instance

        Args:
            attrs (list): A list of attribute names to retrieve.
            If None, all attributes are retrieved.

        Return:
            A dictionary representing the student instance
        """

        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age,
            }
        else:
            python_attribute = {}
            for item in attrs:
                if hasattr(self, item):
                    python_attribute[item] = getattr(self, item)
            return python_attribute


    def reload_from_json(self, json):
        """
        A public methon that replaces all attributes of the Student instance

        Args:
            json (dict): A dictionary of attributes
        """
        for key, value in json.items():
            setattr(self, key, value)
