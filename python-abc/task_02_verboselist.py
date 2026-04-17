#!/usr/bin/python3
"""
Module defining the VerboseList class which extends the built-in list.
Provides notifications when items are added or removed.
"""


class VerboseList(list):
    """A list that prints a message for every modification."""

    def append(self, item):
        """Adds an item and prints notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends the list and prints count of items added."""
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification before popping an item."""
        # We find the item first so we can print it before it's gone
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
