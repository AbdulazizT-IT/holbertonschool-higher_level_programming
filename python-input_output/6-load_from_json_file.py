#!/usr/bin/python3
"""Module for creating an object from a JSON file."""


import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename: The name of the JSON file to load from.

    Returns:
        The Python object created from the JSON file.
    """

    with open(filename, 'r') as f:
        return json.load(f)
