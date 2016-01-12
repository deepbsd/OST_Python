#!/usr/bin/env python3
#
#
#       subdictclass.py
#
#    Lesson 6: Using 
#        Exceptions Wisely
#
#     by David S. Jackson
#          7/24/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
Project for Lesson 6:  Using Exceptions Wisely...
"""

class SubDict(dict):
    """
    This class subclasses the standard dict class.  Its __init__() method
    should take one argument, which will be used as a default value when a
    non-existent key is accessed (it should also call the standard dict's
    __init__() with no arguments).  Its __getitem__() method should attempt to
    use the standard dict.__getitem__(), but any KeyError exceptions should be
    handled by returning the default value passed to __init__() on creation.
    Write a small test program for your object.

    Note: I chose to create a default value for the default key.  This default
    value gets returned anytime the default key is used...
    """
    
    def __init__(self, default):
        "'default' will be the default value for missing keys..."
        self.default = default
        self.defaultvalue = 'default value'
        #super().__init__(self)
        super().__init__()
        super().__setitem__(self.default, self.defaultvalue)


    def __getitem__(self, key):
        "Use some exception handling if no 'key' exists"
        try:
            return super().__getitem__(key)
        except KeyError:
            try:
                #print("trying default key...")
                return super().__getitem__(self.default)

            except KeyError:
                print("Dammit!  We came, we tried, we bombed out and failed...")




