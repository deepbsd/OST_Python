#!/usr/bin/env python3
#
#
#            arr.py
#
#    Lesson 8: Advanced Generators
#
#     by David S. Jackson
#          8/3/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
Project:
    Write a program that uses timeit() to show the difference between a list
    comprehension and the list() function applied to:
    * a list of a million random numbers.
    * a generator that generates a sequence of a million random numbers.
"""


from random import random
from timeit import timeit


# Names for speed values...
speeds_list = ["Speed of List Comp.:", "Speed of Generator:"]

# Different expressions for list comprehension and generator
expressions = [
        "[random()*10 for n in range(1000000)]", 
        "(random()*10 for n in range(1000000))"]


# Calculate and display the values...
print()
for n in range(2):
    speed = timeit("expressions[n]", "from __main__ import n, expressions, random", number=1)
    print("{0:19}\t{1:.15f}  seconds".format(speeds_list[n], speed))
print()


