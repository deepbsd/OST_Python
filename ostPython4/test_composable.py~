#!/usr/bin/env python3
#
#
#       test_composable.py
#
#    Lesson 1: Going Further 
#        With Functions
#
#     by David S. Jackson
#          6/18/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
test_composable.py: performs simple tests of composable functions.
"""

import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x*x

def pwr(x, y):
    "raise x to the power of y"
    return x**y


class ComposableTestCase(unittest.TestCase):

    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)

    def test_pow(self):
        for a in (2,3,4,5,6):
            raizit = Composable(pwr)
            cuber = raizit(a, 3)
            b = a**3
            self.assertEqual(cuber, b)

    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1,1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)

    def test_exceptions(self):
        fc = Composable(square)
        pc = Composable(pwr)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(ValueError):
            pc = pc ** -3
        with self.assertRaises(TypeError):
            pc = pc ** 'a'

if __name__ == "__main__":
    unittest.main()
