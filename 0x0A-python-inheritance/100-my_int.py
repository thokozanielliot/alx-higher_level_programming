#!/usr/bin/python3
"""Define class MyInt that inherits form int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == operator with !="""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with =="""
        return self.real == value
