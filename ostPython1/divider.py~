#!/usr/bin/env python3
#
#
#         divider.py
#
#    Lesson 15: Data Structures
#
#     by David S. Jackson
#          12/24/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
""" 
This project tests more of your understanding of exception handling.

Objective:

This project tests more of your understanding of exception handling.

    1. Create a new Python source file named divider.py.
    2. Create a while loop, request an integer value from the user, and bind the value as an integer to a variable.
    3. Then divide the value of 10 by your new integer and print the results.
    4. Use a try statement followed by a series of except statements to catch ValueError and ZeroDivisionError. When those errors are caught, print response statements to the user informing them of their mistake.

Below is an example of possible output from running the program.

Dividing 10 by an integer
Provide an integer: Steve
Your input must be an integer
Provide an integer: 4
2.5
Provide an integer: 3
3.33333333333
Provide an integer: 2
5.0
Provide an integer: 1
10.0
Provide an integer: 0
Your input must not be zero (0)
Provide an integer:

"""


print("Dividing 10 by an integer...")
while True:
    inp = input("Please enter an integer: ")
    if inp == "":
        print("Bye!")
        break
    try:
        result = 10 / int(inp)
    except ZeroDivisionError:
        print("***Warning*** Input must not be zero (0)")
    except (TypeError, ValueError):
        print("That's not an integer.")
    else:
        print("10 divided by {0} is {1}".format(inp, result))



