#!/usr/bin/python3
"""Module for write_file"""


def write_file(filename="", text=""):
    """Function for write_file"""

    with open(filename, 'w', encoding='UTF-8') as f:
        print(f.write(text), end="")
    return len(text)
