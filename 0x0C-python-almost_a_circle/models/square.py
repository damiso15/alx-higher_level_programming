#!/usr/bin/pythom3
"""
A class Square
"""
from models.rectangle import Rectangle



class Square(Rectangle):
    """
    A class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        A class constructor:

        Args:
            size (int): The size of the square
            x (int): The x-axis of the square
            y (int): the y-axis of the square
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        The __str__ method returns the rectangle as a string
        """
        class_name = "[{}] ".format(self.__class__.__name__)
        string = "({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

        return class_name + string
