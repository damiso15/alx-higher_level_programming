#!/usr/bin/python3
"""
A class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A class constructor

        Attributes:
            width (int): the width of the ractangle
            height (int): the height of the rectangle
            x (int): the x-axis of the rectangle
            y (int): the y-axis of the rectangle
            id (int): the id
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        The property for the width module to retrieve it
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        The property setter for the width module to set it

        Attributes:
            value (int): The widht of the rectangle
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        The property for the height module to retrieve it
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        The property setter for the height module to set it

        Attributes:
            value (int): The height of the rectangle
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        The property for the x module to retrieve it
         """

        return self.__x

    @x.setter
    def x(self, value):
        """
        The property setter for the x module to set it

        Attributes:
            value (int): The x of the rectangle
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        The property for the y module to retrieve it
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        The property setter for the y module to set it

        Attributes:
            value (int): The y of the rectangle
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Public method to calculate the area of a rectangle

        Args:

        Returns:
            The area value of the Rectangle instance
        """

        return self.width * self.height

    def display(self):
        """
        A public method that prints the character # to stdout
        """

        print("{}".format("\n") * self.y, end="")

        for _ in range(self.height):
            print("{}".format(" ") * self.x, end="")
            print("{}".format("#") * self.width)

    def __str__(self):
        """
        The __str__ method returns the rectangle as a string
        """

        class_name = "[{}] ".format(self.__class__.__name__)
        string = "({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                             self.width, self.height)

        return class_name + string

    def update(self, *args, **kwargs):
        """
        A public method that assigns an argument to each attributes

        args:
            args (list): A non keyworded argument
            kwargs (dict): A keyworded argument
        """

        arg_list = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for item, element in enumerate(args):
                if item < len(arg_list):
                    setattr(self, arg_list[item], element)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
