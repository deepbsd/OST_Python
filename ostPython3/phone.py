#!/usr/bin/env python3

"""
Demonstrate use of re.findall()
"""

import re

text = """While I was at the store I tried to call 555-123-4567 on my mobile
but accidentally called 555-754-4321.  The person on the line redirected
me to 999-999-9999 which I don't think is a real number.  Neither is
000-000-0000 or 555-555-0000.
Well, I will try (555) 123-4567 again now.
"""

def get_phone(text):
    "scan a text, locating telephone numbers."
    # Note the use of a 'raw' string constant

    # original re:
    #return re.findall(r"\d\d\d-\d\d\d-\d\d\d\d", text)

    ###  RE modified so it gets all 6 phone numbers
    return re.findall(r"\(*\d\d\d\)*\-* *\d\d\d-\d\d\d\d", text)


if __name__ == '__main__':
    print(get_phone(text))
