#!/usr/bin/python3


"""Module for serialize and save to file and load and deserialize."""


import json


def serialize_and_save_to_file(data, filename):

    """Returns the JSON string representation of a Python object."""

    y = json.dumps(data)
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(y)

def load_and_deserialize(filename):

    """Returns the JSON string representation of a Python object."""

    with open(filename, 'r', encoding='UTF=8') as f:

        data_text = f.read()
        y = json.loads(data_text)
        return y
