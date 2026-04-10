#!/usr/bin/python3
"""Module for creating Square class"""


class Square:
    """A class representing Square"""

    def __init__(self, size=0):
        """Instantiation with a given size"""
        self.size = size

    @property
    def size(self):
        """Getter for the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return of the area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
