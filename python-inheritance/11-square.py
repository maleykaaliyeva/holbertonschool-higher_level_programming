#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
This version includes a custom string representation.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.
        Format: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
