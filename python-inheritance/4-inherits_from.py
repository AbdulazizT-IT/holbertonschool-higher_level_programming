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
    if type(obj) is a_class:
        return False
    else:
        return True
