#!/usr/bin/python3
"""Check if classes are same"""


def is_same_class(obj, a_class):
    """
    Function that returns True/False if the object is exactly
    an instance of the specified class

    Args:
        obj: Object
        a_class: Class type

    Returns:
        True if type of obj is of a_class
        False, otherwise
    """
    return type(obj) is a_class
