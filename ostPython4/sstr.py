#!/usr/bin/env python3
#
#
#         sstr.py
#
#    Lesson 13: Functions and 
#        Other Objects
#
#     by David S. Jackson
#          8/21/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
Project:
    Write a subclass sstr of the standard str type that implements the "<<" and
    ">>" methods as a cyclic shifting of the characters in the string.  It
    should pass the following tests, which you should embody as unit tests in a
    separate test module:

    >>> s1 = sstr("abcde")
    >>> s1 << 0
    'abcde'
    >>> s1 >> 0
    'abcde'
    >>> s1 << 2
    'cdeab'
    >>> s1 >> 2
    'deabc'
    >>> s1 >> 5
    'abcde'
    >>> (s1 >> 5) << 5 == 'abcde'
    True

"""

class sstr(str):
    "This subclass includes << and >> for strings"
    def __init__(self, string):
        self.string = string

    def __lshift__(self, value):
        value = int(value)
        return sstr(self.string[value:] + self.string[:value])

    def __rshift__(self, value):
        value = int(value)
        return sstr(self.string[-value:] + self.string[:-value])





