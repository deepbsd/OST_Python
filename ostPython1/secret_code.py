#!/usr/bin/env python3
#
#
#       secret_code.py
#
#    Lesson 2: Data Structures
#
#     by David S. Jackson
#          12/2/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
"""
Objective:

This project requires you to use built-in functions to perform character manipulations.

    Create a new Python source file named secret_code.py.
    Write a program to read a line of input from the user, and encode it using the following cipher:
    Take each character of the string individually, and make the corresponding character in the output string be that whose ordinal value is 1 more than the ordinal value of the input character. Once the output string has been constructed in this way, the output of the program should be the reverse of the constructed output string.

Below is an example of possible input and output from running the program.

Message: This is it
uj!tj!tjiU

"""

r_ciph = ""
user_text = input("Please enter text to encode: ")
for c in reversed(user_text):
    r_ciph += chr(ord(c)+1)
    
print("Secret code: ",r_ciph)
