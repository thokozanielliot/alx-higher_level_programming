#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _keys = list(a_dictionary.keys())
    for key in _keys:
        if value == a_dictionary.get(key):
            del a_dictionary[key]
    return a_dictionary
