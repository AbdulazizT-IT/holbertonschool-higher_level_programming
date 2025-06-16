#!/usr/bin/python3


"""Module for converting Python objects to JSON string representation."""


import json


def from_json_string(my_str):

    """
    Returns the JSON string representation of a Python object.

    Args:
        my_str: The Python object to convert (e.g. dict, list, etc.)

    Returns:
        obj: The JSON string representation of the object.
    """

    return json.loads(my_str)
