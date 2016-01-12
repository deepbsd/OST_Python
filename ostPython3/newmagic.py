#!/usr/bin/env python3

'''
Python classes with magic methods
'''

class ustr(str):
    "An upper case string object."
    def __new__(cls, arg):
        arg = str(arg)
        return str.__new__(cls, arg.upper())

