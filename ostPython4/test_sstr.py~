#!/usr/bin/env python3
#
#
#       test_sstr.py
#
#    Lesson 13: Functions and
#         Other Objects
#
#     by David S. Jackson
#          8/15/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
Project:
    Write a subclass sstr of the standard str type that implements the "<<" and
    ">>" methods as a cyclic shifting of the characters in the string.  It
    should pass the following tests, which you should embody as unit tests in a
    separate test module:

    >>> s1 = sstr("abcde")
    >>> s1 << 0
    'abcde'
    >>> s1 >> 0
    'abcde'
    >>> s1 << 2
    'cdeab'
    >>> s1 >> 2
    'deabc'
    >>> s1 >> 5
    'abcde'
    >>> (s1 >> 5) << 5 == 'abcde'
    True

"""

from sstr import sstr
import unittest


class TestSstr(unittest.TestCase):

    def setUp(self):
        self.s1 = sstr('abcde')


    def test_lshft(self):
        expected0 = 'abcde'
        expected2 = 'cdeab'
        expected5 = 'abcde'
        self.assertEqual(self.s1 << 0, expected0)
        self.assertEqual(self.s1 << 2, expected2)
        self.assertEqual(self.s1 << 5, expected5)

    def test_rshft(self):
        expected0 = 'abcde'
        expected2 = 'deabc'
        expected5 = 'abcde'
        self.assertEqual(self.s1 >> 0, expected0)
        self.assertEqual(self.s1 >> 2, expected2)
        self.assertEqual(self.s1 >> 5, expected5)

    def test_returntype(self):
        expected = True
        self.assertEqual((self.s1 >> 5) << 5 == 'abcde', expected)


if __name__ == "__main__":
    unittest.main()



