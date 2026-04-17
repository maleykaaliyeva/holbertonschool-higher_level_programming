#!/usr/bin/python3
"""
This module defines the SwimMixin and FlyMixin classes,
and a Dragon class that inherits from both.
"""


class SwimMixin:
    """A mixin that provides swimming behavior."""
    def swim(self):
        """Prints a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying behavior."""
    def fly(self):
        """Prints a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits from SwimMixin and FlyMixin.
    It can swim, fly, and roar.
    """
    def roar(self):
        """Prints a message indicating the dragon is roaring."""
        print("The dragon roars!")
