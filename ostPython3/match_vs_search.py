#!/usr/bin/env python3

"""
Demonstrate the difference between match() and search()
"""

import re

def check_number(text):
    #regex = r"\d\d\d-\d\d\d-\d\d\d\d"  # first draft
    regex = r"(\d\d\d|\(\d\d\d\))(-| )\d\d\d-\d\d\d\d"
    # I would try something a little more sensible...
    regex1 = r"(\(*\d{3}\)*)(-| )(\d{3}-\d{4})"
    match = re.match(regex1, text)
    if match:
        return match.group()

    match = re.search(regex1, text)
    if match:
        return len(text)
