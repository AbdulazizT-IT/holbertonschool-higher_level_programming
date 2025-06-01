#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math
"""Shape class."""


class Shape(ABC):
    """Initializes an Shape instance"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return abs(self.radius * self.radius) * math.pi

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self. width * self. height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
