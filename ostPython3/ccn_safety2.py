#!/usr/bin/env python3
#
#
#         ccn_safety.py
#   
#    Lesson 6: Compiling and Flagging Regexes
#
#       by David S. Jackson
#           4/30/2015
#
#   OST Python3: The Python Environment
#      for Kirby Urner, Instructor
#
#
"""
This program extends the method from Lesson 5 by compiling the regex
"""

text = """Have you ever noticed, in television and movies, that phone numbers
and credit cards are obviously fake numbers like 555-123-4567 or
5555-5555-5555-5555? It is because a number that appears to be real, such as
1234-5678-1234-5678, triggers the attention of privacy and security experts."""



import re

def num_safe(mytext):
    "Swtiches to using 'compiled' regex, also re.X switch"
    regex = re.compile(r"""
    \d{4}              # first 4 digits
    ((-|\s)\d{4}){3}   # match CCNs with dashes or spaces
    """, re.VERBOSE)
    replacewith = "CCN REMOVED FOR YOUR SAFETY"
    return regex.sub(replacewith, mytext)


if __name__ == "__main__":
    result = num_safe(text)
    print(result) 
