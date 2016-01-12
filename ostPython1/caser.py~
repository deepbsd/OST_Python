#!/usr/bin/env python3
#
#
#           caser.py
#
#    Lesson 13: More About 
#           Functions
#
#     by David S. Jackson
#          12/6/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#

""" Modifies the case of inputted text.  User selects from a menu
    capitalize:  accepts string and applies the capitalize() method
    title:       accpets string and applies title() method
    upper:       accpets a string and applies upper() method
    lower:       accepts a string and applies lower() method
"""

import sys         # so we can use the exit() method

def capitalize(usr_string):
    """ applies the capitalize() string method """
    return usr_string.capitalize()

def title(usr_string):
    """applies the title() string method to usr string"""
    return usr_string.title()

def upper(usr_string):
    """applies the upper() method to usr string"""
    return usr_string.upper()

def lower(usr_string):
    """applies the lower() method to usr string"""
    return usr_string.lower()

def exit(usr_string):
    """terminates program"""
    print("Exiting now.  Bye!")
    sys.exit()


if __name__ == "__main__" :

    # Today is 8/8/15.  Today I wouldn't call seperate functions like I
    # did in this exercise.  I would probably just go 'mystr.capitalize' 
    # and eval(mystr).  Not even have functions in the program.  But this
    # program was about functions!!!

    switch = {
            'capitalize': capitalize,
            'title': title,
            'upper': upper,
            'lower': lower,
            'exit': exit
    }

    options = switch.keys()
    prompt = 'Pick an option from the list ({0}): '.format(', '.join(options))
    while True:
        inp = input(prompt)
        # instructions specify must ask for string before exit...
        #if inp == 'exit':
        #    print('Bye! Thanks for playing!')
        #    break
        option = switch.get(inp, None)
        if option:
            inp2 = input("Enter a string: ")
            # could go print(option(inp2)) if switch values were 'str.upper' etc
            # Then I wouldn't need all those functions...
            # But I hadn't heard the term 'refactoring' yet...
            print(option(inp2))
        else:
            print("Please select a valid option!")
