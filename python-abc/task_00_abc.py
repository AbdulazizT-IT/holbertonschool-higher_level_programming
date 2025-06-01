#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Animal class."""

class Animal(ABC):
    """Initializes an Animal instance"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"



