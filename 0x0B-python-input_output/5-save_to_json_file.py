#!/usr/bin/python3
"""Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text fle using JSON representation

    Args:
        my_obj (any): Object
        filename (str): Name of file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
