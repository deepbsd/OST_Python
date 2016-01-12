#!/usr/bin/env python3
#
#
#       find_regex.py
#
#    Lesson 4: Basic Regex
#
#     by David S. Jackson
#          4/27/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
This simple program function finds a regex pattern inside a piece of text
and returns a re search object containing that information.
This assignment wanted to find the phrase 'Regular Expressions'.  It 
should start at character 231 and end at character 250.
"""

import re

text = """\
In the 1950s, mathematician Stephen Cole Kleene described automata theory and
formal language theory in a set of models using a notation called "regular
sets" as a method to do pattern matching. Active usage of this system, called
Regular Expressions, started in the 1960s and continued under such pioneers as
David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry
Spencer. 
"""

def findregex(intext):
    """
    Accepts 'text' as input; finds 'Regular Expressions' in text, 
    returns SRE match object
    """
    pattern = "(Regular) (Expressions)"
    m = re.search(pattern, intext)
    return m


if __name__ == "__main__":
    thing = findregex(text)
    print("string equals: {}".format(thing.group()))
    print("Starts: {}, Ends: {}".format(thing.start(), thing.end()))


