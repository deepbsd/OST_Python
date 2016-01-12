#!/usr/bin/env python3
#
#
#       adder.py
#
#    Lesson 1: User Input
#
#     by David S. Jackson
#          4/21/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
adder.add2() simply adds two integers together after verifying that they
both are in fact integers.  If they are not, a TypeError is raised and the
function errors out.
"""

def add2(num_a, num_b):
    "adds two integers a and b.  verifies whether they are indeed integers."

    if type(num_a) == type(1) and type(num_b) == type(1):
        return num_a + num_b
    else:
        print("INTEGERS ONLY PLEASE!")
        raise TypeError


if __name__ == "__main__":
    print("the sum is: ", add2(4, 5))
    print("the sum is: ", add2(124, 465))
    #print(add2('one', 'two'))   # debugging
    #print(add2('one', 2))       # debugging
