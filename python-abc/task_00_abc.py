#!/usr/bin/python3
"""
Module for Abstract Animal Class
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound"""
        pass


class Dog(Animal):
    """Subclass Dog inheriting from Animal"""

    def sound(self):
        """Returns the bark sound"""
        return "Bark"


class Cat(Animal):
    """Subclass Cat inheriting from Animal"""

    def sound(self):
        """Returns the meow sound"""
        return "Meow"
