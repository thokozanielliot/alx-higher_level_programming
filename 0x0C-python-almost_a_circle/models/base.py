#!/usr/bin/python3
""""Define a base class Base"""


class Base:
    """Represents a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize instances

        Args:
            id (int): ID of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
