#!/usr/local/bin/python3
#
#      Adds numbers, strings, lists, together
#
#      testadder.py  for OST Python2 Lesson 3
#
#         Copied for Lesson 3 from text
#            by David S. Jackson
#
#          Instructor: Pat Barton
#
"""
Demonstrates the fundamentals of unittest.
adder() is a function that lets you 'add' integers,
strings and lists.
"""

from adder import adder  # keep the tested code separate from the tests

import unittest

class TestAdder(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(adder(3,4), 7, "3 + 4 should be 6")

    def test_strings(self):
        self.assertEqual(adder('x','y'), 'xy', "x + y should be xy")

    def test_lists(self):
        self.assertEqual(adder([1,2],[3,4]), [1,2,3,4], "[1,2] + [3,4] should be [1,2,3,4]")

    def test_number_and_strings(self):
        self.assertEqual(adder(1,'two'), '1two', "1 + two should be 1two")

    def test_numbers_and_list(self):
        self.assertEqual(adder(4,[1,2,3]), [1,2,3,4], "4 + [1,2,3] should be [1,2,3,4]") 

if __name__ == "__main__":
    unittest.main()



