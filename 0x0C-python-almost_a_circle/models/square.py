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

    @property
    def size(self):
        """
        The property for the size module to retrieve it
        """

        return self.__width

    @size.setter
    def size(self, value):
        """
        The property setter for the y module to set it

        Attributes:
            value (int): The size of the rectangle
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        A public method that assigns an argument to each attributes

        args:
            args (list): A non keyworded argument
            kwargs (dict): A keyworded argument
        """

        arg_list = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for item, element in enumerate(args):
                if item < len(arg_list):
                    setattr(self, arg_list[item], element)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        A public class method that returns the dictionary representation of a Square

        Returns:
            The dictionary representation
        """

        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
