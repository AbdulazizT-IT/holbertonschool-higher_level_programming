#!/usr/bin/python3
import json
"""Module for converting Python objects to JSON string representation."""

def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.

    Args:
        my_obj: The Python object to convert (e.g. dict, list, etc.)

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
