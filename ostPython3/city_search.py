#!/usr/bin/env python3

"""
String regular expressions
"""

import re

def city_search(text):

    #regex = r"[A-Z][a-z]+(\s[A-Z][a-z]+)*,\s[A-Z]{2}\s\d{5}"
    regex = re.compile(r"""
        [A-Z][a-z]+             # the first word of a city
        (\s[A-Z][a-z]+)*        # possible additional words of a city
        ,\s[A-Z]{2}\s           # The two-letter abbreviation for a US state
        \d{5}(-\d{4})?          # 5 or 9 digit zip code
        """, re.X)

    # re.X above means same as re.VERBOSE
    #search = re.search(regex, text)
    search = regex.search(text)

    if search:
        return search.group()


