#!/usr/bin/python3
"""Module for read_file"""


def read_file(filename=""):
    """Function for read_file"""

    with open(filename, 'r', encoding='UTF-8') as f:
        print(f.read())