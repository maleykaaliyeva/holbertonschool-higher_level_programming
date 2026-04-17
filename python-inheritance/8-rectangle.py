#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
It represents a basic rectangle shape with width and height.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle, inheriting from BaseGeometry.
    Attributes:
        __width (int): Private width of the rectangle.
        __height (int): Private height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Note:
            Both width and height are validated using the integer_validator
            method inherited from the BaseGeometry class.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
