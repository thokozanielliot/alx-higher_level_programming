#!/usr/bin/python3
"""Define an inherited class-checking function"""


def inherits_from(obj, a_class):
    """
    Functions that returns True/False if the obj is an instance
    of a class that inherited (directly/indirectly) from the specified class

    Args:
        obj: Object
        a_class: Class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
