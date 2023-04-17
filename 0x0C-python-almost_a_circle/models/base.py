#!/usr/bin/python3
"""
A first class Base
"""


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
