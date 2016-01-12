#!/usr/bin/env python3
#
#
#           greeting.py 
#
#    Lesson 2: Entering and Storing Data
#
#     by David S. Jackson 11/25/2014
#   
#  OST Python1: Beginning Python for Pat Barton, Instructor
#
""" 
greeting.py: Takes a first and last name and spits out a string
concatenating both inputs.  
"""

first = input("What is your first name? ")
first = str(first)
second = input("What is your last name? ")
second = str(second)
# Try and do something clever with the data...
message = "None shall pass, "
print(message, first, second)



