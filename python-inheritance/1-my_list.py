#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
    MyList inherits from list and adds a method to print the sorted list
    """

    def print_sorted(self):
        print(sorted(self))
