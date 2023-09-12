#!/usr/bin/python3
"""Define a object to JSON string"""
import json


def to_json_string(my_obj):
    """
    Function that returns JSON representation of an object

    Args:
        my_obj: Object

    Raises:
        Exception: When the object can't be encoded
    """
    return json.dumps(my_obj)
