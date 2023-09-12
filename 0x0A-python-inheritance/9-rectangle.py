#!/usr/bin/python3
"""Define a rectangle class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""

    def __init__(self, width, height):
        """
        Function that instantiations instances

        Args:
            width (int): Width of rectangle
            height (int): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returns the are of the instances"""
        return self.__width * self.__height

    def __str__(self):
        """Special method that returns the printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
