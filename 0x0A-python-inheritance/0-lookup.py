#!/usr/bin/python3
def lookup(obj):
    """
    Function that returns the list of available
    attributes & methods of an object

    Args:
        obj: Instance of the class

    Return:
        List of object
    """
    return dir(obj)
