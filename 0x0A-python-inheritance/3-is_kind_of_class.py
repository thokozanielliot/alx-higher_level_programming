#!/usr/bin/python3
"""Checks if obj is an instance or inherited from"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True/False if the obj is an instance of
    or if the obj is an instance of a class that inherited from
    the specified class

    Args:
        obj: Object
        a_class: Class type

    Returns:
        True if obj is an instance
        True if obj is an instance of a class inherited from
        False, otherwise
    """
    return isinstance(obj, a_class)
