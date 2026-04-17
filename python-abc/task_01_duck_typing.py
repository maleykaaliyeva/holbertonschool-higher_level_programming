#!/usr/bin/python3
"""Module containing Shape class and its inheritances"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """The Shape class"""

    @abstractmethod
    def area(self):
        """Method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method for perimeter"""
        pass


class Circle(Shape):
    """The Circle class inherited from Shape"""

    def __init__(self, radius):
        """Initialization with radius"""
        self.radius = radius

    def area(self):
        """Returning area"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returning perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """The Rectangle class inherited from Shape"""

    def __init__(self, width, height):
        """Initialization with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returning area"""
        return self.width * self.height

    def perimeter(self):
        """Returning perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function to give shape info"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
