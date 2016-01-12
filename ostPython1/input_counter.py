#!/usr/bin/env python3
#
#
#      input_counter.py 
#
#    Lesson 6: Sets and Dicts
#
#     by David S. Jackson
#          11/29/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
"""

This program gets user input (a sentence of some kind) and parses the words
into a list of words, and then loops through the list and adds each word to a
set.  Another loop creates a dict of these words with the index being the
numeric order the words were discovered in.

"""

# Empty start for dict and set
input_set = {""}
input_dict = {}


# Get user input...
while True:
    user_input = input("<Enter> to quit or...\nPlease input text: ")
    if user_input == "" :
        break
    user_input = user_input.lower().split()
    # input_set has one space in it on first iteration, which I don't count
    if len(input_set) == 1:
            former_set_length = 0
    else:
        former_set_length = len(input_set)
    # add *unique* entries from set to a dict...
    for word in user_input:
        input_set.add(word)
        # 'not in' part makes program work with unlimited inputs from user
        if len(input_set) > former_set_length:
            input_dict[word] = len(input_set)-1

    # print the keys and values...
    for word, order_discovered in input_dict.items() :
        print(word, "-->", order_discovered)



print("All finished! ")











