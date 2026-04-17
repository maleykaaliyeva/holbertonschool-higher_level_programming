#!/usr/bin/python3
"""
Module for CountedIterator class.
This class wraps an iterator and tracks the number of items fetched.
"""


class CountedIterator:
    """
    A class that extends the functionality of a standard iterator
    by keeping track of the iteration count.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator object and a counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current value of the counter.
        """
        return self.counter

    def __next__(self):
        """
        Increments the counter and returns the next item.
        Raises StopIteration when no more items are available.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
