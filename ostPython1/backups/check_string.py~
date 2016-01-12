#!/usr/bin/env python3
#
#
#        check_string.py
#
#    Lesson 3: Making Decisions: 
#              The if Statement
#
#     by David S. Jackson
#          11/25/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
"""
Program asks for user input in UPPER CASE STRING ending with a "."
Then the program checks to see if user comlied with those two requirements
and prints errors and requires correct input before exiting.
I'm trying to think about sanitizing input a little bit here...
"""


done = False

while done == False :
    print("Done = ", done)
    my_str = input("Please enter an upper-case string ending with a period: ")
    my_str = str(my_str)
    if not my_str.isupper() :
        print("Didn't enter ALL UPPER CASE STRING.")
        done = False
    elif not my_str.endswith(".") :
        print("Didn't end string with a '.'")
        done = False
#    elif not my_str.isalnum() :
#        print("You didn't print alpha numeric characters!")
#        done = False
    elif my_str.isupper() and my_str.endswith(".") :
        print("Well done!  You can follow directions!")
        done = True
    else :
        print("You messed up somehow...")
        done = False


