#!/usr/bin/python3
"""
This module provides a class that inherits from the standard list.
"""


class MyList(list):
    """
    A class that adds a specialized sorting display to list objects.
    """

    def print_sorted(self):
        """
        Prints the current elements of the list in ascending order.
        """
        print(sorted(self))
