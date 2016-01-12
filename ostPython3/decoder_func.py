#!/usr/bin/env python3
#
#
#       decoder_func.py
#
#    Lesson 3: Iteration in Python
#
#     by David S. Jackson
#          4/25/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#

"""
I figured I could use the practice solving this problem both ways.

In addition to the create a class of iterator method, this 
generator function also works for a solution.
"""

def alphabator(m):
    "This is the function way to solve the Lesson 3 Project"
    n = 0
    for item in m:
        n += 1
        if (type(item) == type(1)) and (item >= 1 and item <= 27):
            item = chr(64 + item)
        yield item
