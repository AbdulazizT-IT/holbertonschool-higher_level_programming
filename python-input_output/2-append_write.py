#!/usr/bin/python3
"""Module for append_file"""


def append_write(filename="", text=""):
    """Function for append_file"""

    with open(filename, 'a', encoding='UTF-8') as f:
        return (f.write(text))
