#!/usr/bin/python3
"""
Defines a Student class with first_name, last_name, age,
and provides a method to retrieve its dictionary representation
with optional attribute filtering.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(elem, str) for elem in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
