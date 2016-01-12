#!/usr/bin/env python3
#
#
#       test_decoder.py
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
test_decoder.py is actually part of the Lesson 3 Project
definition.  I didn't have to create this myself; it was
already specified in the project definition assignment.
"""

import unittest
from string import ascii_uppercase
#from decoder import alphabator   # works fine 
from decoder_func import alphabator  # try with generator...

class TestAlpha(unittest.TestCase):

    def test_easy_26(self):
        a = alphabator(range(1, 27))
        self.assertEqual(list(ascii_uppercase), list(a))

    def test_upper_range(self):
        a = alphabator(range(40, 50))
        self.assertEqual(list(range(40, 50)), list(a))

    def test_various_objects(self):
        l = ['python', object, ascii_uppercase, 10, alphabator]
        a = list(alphabator(l))
        self.assertNotEqual(l[3], a[3])
        self.assertEqual("J", a[3])
        self.assertTrue(isinstance(a[1], object))


if __name__ == "__main__":

    unittest.main()



