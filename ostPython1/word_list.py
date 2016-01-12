#!/usr/bin/env python3
#
#
#         word_list.py
#
#    Lesson 5: Sequence Containers: 
#         Lists and Tuples
#
#     by David S. Jackson
#          11/26/2015
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
"""
Get a string from user with upper case and lower case words
Create a list of words with only lower case letters and another list with
upper case letters.  Two lists.  Print out each list and the words in them.
"""

da_string = input("Please input your text: ")

lc_list = []
UC_list = []

for word in da_string.split(" "):
    if word.islower():
        lc_list.append(word)
    else:
        UC_list.append(word)
    """
    for c in word :
        if c.isupper() :
            # the 'break' prevents duplicate words in list when there are
            # multiple UC characters in word.
            UC_list.append(word)
            break
    """

for word in UC_list + lc_list :
    print(word)
