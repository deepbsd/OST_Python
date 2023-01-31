#!/usr/bin/env python3

"""Program to locate the first space in the input string."""

"""NOTE:  the example in the book had a problem.  I rewrite the program to fix it"""

s = input("Please enter a string: ")
pos = 1
spaces = 0
for c in s:
    if c == " ":
        spaces += 1
        print("First space occurred at position: ", pos)
        break
    pos += 1 

if spaces == 0:
    print("No spaces in that string.")


