#!/usr/bin/python3
"""Module for saving an object to a file as JSON string."""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename: The name of the file to write to.
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
