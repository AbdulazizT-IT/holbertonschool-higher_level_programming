#!/usr/bin/python3
"""
This module defines a function that returns Ture if the object is an instance
of a class that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True or False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
