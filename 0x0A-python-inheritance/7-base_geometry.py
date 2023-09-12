#!/usr/bin/python3
"""Define a base geometry class BaseGeometry"""


class BaseGeometry:
    """REpresent a base geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates an integer

        Args:
            name(string): Name
            value(int): Value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
