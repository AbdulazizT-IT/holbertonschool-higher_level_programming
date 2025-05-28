#!/usr/bin/python3
"""
This module defines a function that return True if the obj
is exactly an instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns True or False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
