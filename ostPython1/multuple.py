#!/usr/bin/env python3
#
#
#            multiple.py
#
#    Lesson 7: String Formatting
#
#     by David S. Jackson
#          11/30/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#

""" 
takes as data a tuple of two-element tuples, such as ((1,1), 2,2), (12,13),
(4,4), (99,98)).  This and/or similar data should be hard-coded (no need for
user input).  Loop over the tuple and print out the results of multiplying the
numbers together, and use string formatting to display nicely.  
""" 

my_tuple = ( (8, 9), (11, 13), (4, 5), (19, 23), (9, 18))

for n1, n2 in my_tuple :
    print("{0:2d}{a:^5}{1:2d}{b:>4}{2:4d}".format(n1, n2, n1*n2, a="X", b="="))


