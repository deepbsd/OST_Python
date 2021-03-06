#!/usr/bin/env python3
#
#
#         ccn_safety.py
#   
#    Lesson 5: More on Regex
#
#       by David S. Jackson
#           4/28/2015
#
#   OST Python3: The Python Environment
#      for Kirby Urner, Instructor
#
#
"""
This module includes the num_safe method, which takes a text and
returns any credit card numbers in the form of 1234-1234-1234-1234
and returns them in the form of XXXX-XXXX-XXXX-1234.

Additionally, numbers in the form of 1234 1234 1234 1234 are also 
returned as XXXX-XXXX-XXXX-1234.

'text' variable is a string taken from the Project Assignment.
"""

text = """Have you ever noticed, in television and movies, that phone numbers
and credit cards are obviously fake numbers like 555-123-4567 or
5555-5555-5555-5555? It is because a number that appears to be real, such as
1234-5678-1234-5678, triggers the attention of privacy and security experts."""



import re

def num_safe(mytext):
    pattern = r"\d{4}(-| )\d{4}(-| )\d{4}(-| )"
    return re.sub(pattern, "XXXX-XXXX-XXXX-", mytext)


if __name__ == "__main__":
    result = num_safe(text)
    print(result) 
