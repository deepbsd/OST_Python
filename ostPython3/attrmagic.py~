#!/usr/bin/env python3

'''
Demonstrate magic methods for attribute access.
'''

class AttrMixin:
    "Displays a message when an instance's attributes are set."
    def __setattr__(self, key, value):
        print("ATTR: setting attribute {0!r} to {1!r}".format(key, value))
        self.__dict__[key] = value

    def __getattr__(self, key):
        print("ATTR: getting attribute {0!r}".format(key))
        return "No Value"

    def __delattr__(self, key):
        print("ATTR: Deleting key {0!r}".format(key))
        object.__delattr__(self, key)


class Person(AttrMixin):
    "Represents a person"
    def __init__(self, name):
        self.name = name

