#!/usr/bin/python3
"""Define a class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize instances

        Args:
            size (int): Size of Square
            x (int): x coordinate of Square
            y (int): y coordinate of Square
            id (int): Id of Square
        """
        super().__init(size, size, x, y, id)

    def __str__(self):
        """Special way of printing"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
