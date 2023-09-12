#!/usr/bin/python3
"""Defines an object attribute"""


def lookup(obj):
    """Return a list of an objects available attributes"""
    return dir(obj)
