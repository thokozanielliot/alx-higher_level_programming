#!/usr/bin/python3
"""Define a square class that inherits from class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """Initialize instances"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method returns area"""
        return super().area()

    def __str__(self):
        """Special method that returns a printable string"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
