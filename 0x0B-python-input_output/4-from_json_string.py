#!/usr/bin/python3
"""Define JSON string to Object"""
import json


def from_json_string(my_str):
    """
    Function that returns an object represented by a JSON string

    Args:
        my_str (str): String

    Raise:
        Exception: If the JSON string doesn't represent an object
    """
    return json.loads(my_str)
