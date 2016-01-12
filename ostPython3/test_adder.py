#!/usr/bin/env python3
#
#
#      test_adder.py
#
#    Lesson 1: User Input
#
#     by David S. Jackson
#          4/21/15
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
test_adder.py checks to see whether adder.add2() both rejects bad 
user input and accepts good user input, and that the correct
sum is returned for known good inputs to the add2() method.

"""

import unittest
from adder import add2


class Test(unittest.TestCase):
    "tests functionality of adder.add2() method from adder module"

    def test_adder_errors(self):
        "Tests bad input to ensure it is rejected."
        with self.assertRaises(TypeError):
            add2("one", "two", "Accepting strings!")
        with self.assertRaises(TypeError):
            add2("one", 2, "Accepting only one integer!")
        with self.assertRaises(TypeError):
            add2("one", " ", "Accepting a space!")
        with self.assertRaises(TypeError):
            add2(2, "", "Accepting a RETURN!")
        with self.assertRaises(TypeError):
            add2('2', 4, "Accepting a string as a number!")
    
    
    def test_adder_success(self):
        "Tests known good input to ensure it is accepted."
        self.assertEqual(add2(5, 8), 13, "Not accepting good input!")
        self.assertEqual(add2(567, 92), 659, "Answer should be 659!")


if __name__ == "__main__":
    unittest.main()
