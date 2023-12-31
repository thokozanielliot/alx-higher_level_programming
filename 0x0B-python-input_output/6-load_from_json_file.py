#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Function that creates an object from a JSON file

    Args:
        filename (str): Name of JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
