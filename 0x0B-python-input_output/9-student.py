#!/usr/bin/python3
"""
A class Student that defines a student by
"""


class Student:
    """
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

    def to_json(self):
        """
        A public method that retrieves a dictionary representation of a
        Student instance

        Return:
            A dictionary representing the student instance
        """

        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
        }
