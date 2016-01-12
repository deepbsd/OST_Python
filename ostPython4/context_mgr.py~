#!/usr/bin/env python3
#
#
#       context_mgr.py
#
#    Lesson 14: Context Managers
#
#     by David S. Jackson
#          8/17/15
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
Project:

    Write a context manager class that suppresses any ValueError
    exceptions that occur in the controlled suite, but allows any
    other exception to be raised in the surrounding context.


"""

class ctx_mgr:

    def __init__(self, raising=True):
        self.raising = raising

    def __enter__(self):
        cm = object()
        return cm

    def __exit__(self, exc_type, exc_val, exc_tb):
        "Self.raising can be overridden, so I reset it excplicitly."
        self.raising = True
        if exc_type == ValueError:
            return self.raising
        elif exc_type:
            raise



if __name__ == "__main__":

    with ctx_mgr(raising=True) as cm:
        print('To create ValueError, enter a float or string.')
        num = int(input("Enter a number: "))
        print('To create an IndexError, enter an int greater than 4.')
        myindex = int(input('lst1 = [1,2,3,4,5].  What index is number 4? '))
        lst1 = [1,2,3,4,5]
        print("The value you selected is: ", lst1[myindex])
        print("Divide by zero!", 3/0)







