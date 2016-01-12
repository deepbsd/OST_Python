#!/usr/bin/env python3
#
#
#      test_context_mgr.py
#
#    Lesson 14: Content Managers
#
#     by David S. Jackson
#          8/17/15
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
Project:
    Write a context manager class that suppresses any ValueError
    exceptions that occur in the controlled suite, but allows any
    other exceptions to be raised in the surrounding context.

This test suite tests that ValueErrors are NOT raised and that
IndexErrors, DivideByZero, TypeError, and KeyErrors ARE raised.
"""

from context_mgr import ctx_mgr
import unittest


class TestContextMgr(unittest.TestCase):

    def test_index_error(self):
        with self.assertRaises(IndexError):
            with ctx_mgr(raising=True) as cm:
                mylst = [1,2,3,4,5]
                print(mylst[7])

    def test_zero_divide(self):
        with self.assertRaises(ZeroDivisionError):
            with ctx_mgr(raising=True) as cm:
                3/0

    def test_type_error(self):
        with self.assertRaises(TypeError):
            with ctx_mgr(raising=True) as cm:
                mylst = [1,2,3,4,5]
                print(mylst['a'])

    def test_key_error(self):
        with self.assertRaises(KeyError):
            with ctx_mgr(raising=True) as cm:
                mydct = {'a':1, 'b':2, 'c':3}
                print(mydct[1])

    def test_no_value_error(self):
        with ctx_mgr(raising=True) as cm:
            self.assertTrue(print(int('abcd')))


if __name__ == "__main__":
    unittest.main()

