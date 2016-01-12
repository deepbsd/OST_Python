#!/usr/bin/env python3
#
#
#       test_find_regex.py
#
#    Lesson 4: Basic Regular 
#          Expressions
#
#     by David S. Jackson
#          4/27/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
This program provides a simple test to the findregex()
function in the find_regex.py program.  It tests that
the start character for the match object is 231 and that the 
end character is 250.  Also, the contents of the object
must equal 'Regular Expressions'.
"""

import unittest
from find_regex import text, findregex



class TestFindRegex(unittest.TestCase):

    def test_startend(self):
        "tests for start of regex"
        expected_start = 231
        expected_end = 250
        expected = (231, 250)
        reobj = findregex(text)
        self.assertEqual(reobj.start(), expected_start)
        self.assertEqual(reobj.end(), expected_end)
        self.assertEqual(reobj.span(), expected)

    def test_contents(self):
        "tests for contents of match object"
        expected = 'Regular Expressions'
        first = 'Regular'
        second = 'Expressions'
        reobj = findregex(text)
        self.assertEqual(reobj.group(1), first)
        self.assertEqual(reobj.group(2), second)
        self.assertEqual(reobj.group(), expected)

    def test_none(self):
        "tests that bad regex is not matched"
        self.assertIsNone(findregex('regular expressions'), msg=None)


if __name__ == "__main__":
    unittest.main()
