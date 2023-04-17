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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """
            The property for the width module to retrieve it
            """

            self.__width


        @width.setter
        def width(self, value):
            """
            The property setter for the width module to set it

            Attributes:
                value (int): The widht of the rectangle
            """

            self.__width = value


        @property
        def height(self):
            """
            The property for the height module to retrieve it
            """

            self.__height

        @height.setter
        def height(self, value):
            """
            The property setter for the height module to set it

            Attributes:
                value (int): The height of the rectangle
            """

            self.__height = value

        @property
        def x(self):
            """
            The property for the x module to retrieve it
            """

            self.__x

        @x.setter
        def x(self, value):
            """
            The property setter for the x module to set it

            Attributes:
                value (int): The x of the rectangle
            """

            self.__x = value

        @property
        def y(self):
            """
            The property for the y module to retrieve it
            """

            self.__y

        @y.setter
        def y(self, value):
            """
            The property setter for the y module to set it

            Attributes:
                value (int): The y of the rectangle
            """

            self.__y = value
