#!/usr/bin/env python3
#
#
#       decoder.py
#
#    Lesson 3: Iteration in Python
#
#     by David S. Jackson
#          4/25/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
decoder.py is an exercise in creating an iterator class which, 
when passed a list, returns each element in that list as 
it is, unless that element is an integer between 1 and 
26.  In that case, the element is translated to to the
corresponding capital letter in the alphabet, such that 
the integer to letter correspondence is 1=A, 2=B, and so 
forth.  This is accomplished through the chr(64+i) built-in, 
where i is the integer between 1 and 26.

Any element of the list that is *not* an integer between 1 
and 26 is returned just as it was in the list originally.  
"""


class alphabator:
    """
    Returns a list of objects, but translates integer values
    between 1 and 26 into capital letters, such that 1=A, 
    2=B, 3=C, and so forth.  All other objects in list are
    returned "as is."
    """

    def __init__(self, lst):
        "Initializes the 'alphabator' object."
        self.lst = lst
        self.itemno = 0
        self.count = 1

    def __iter__(self):
        "This object is not an iterable."
        return self

    def __next__(self):
        "Return the next value in the output sequence."
        if self.count > self.itemno:
            try:
                self.val = self.lst[self.itemno]
                # need to check for val being an integer between 1 and 26
                if (type(self.val) == type(1)) and (self.val >= 1 and self.val <= 26):
                    # if so, change val to the appropriate uppercase letter...
                    self.val = chr(64+self.val)
            except IndexError:
                raise StopIteration
            self.itemno += 1
            # needed to remove the count incrementor here from original lesson
            # example
        self.count += 1
        return self.val







