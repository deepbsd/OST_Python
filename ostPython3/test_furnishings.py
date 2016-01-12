#!/usr/bin/env python3
#
#
#      test_furnishings.py
#
#    Lesson 7: Python's Object
#        Oriented Features
#
#     by David S. Jackson
#          5/3/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
Tests furnishings.py.  This program creates a home list and submits
it to map_the_home() in the furnishings module, and tests to see that
correct values are returned in a 'homedict'.  Also, that home list
object used by map_the_home() is also borrowed for use in test_count().
Since the furnishings.counter() does not return an object, code is used
that is identical to furnishings.counter() to count the types of 
objects in the 
"""

import unittest
from furnishings import *


class TestFurnishings(unittest.TestCase):
    
    def setUp(self):
        "Creates setUp values"
        self.home = []
        self.home.append(Bed('Bedroom'))
        self.home.append(Sofa('Living Room'))
        self.home.append(Bookshelf('Basement'))
        self.home.append(Table('Dining Room'))
        self.home.append(Sofa('Guest Room'))
        self.home.append(Bed('Guest Room'))


    def test_map(self):
        "Tests the homedict that gets returned..."
        homeobj = map_the_home(self.home)
        self.assertIsInstance(homeobj['Guest Room'][1], Bed)
        self.assertIsInstance(homeobj['Bedroom'][0], Bed)
        self.assertIsInstance(homeobj['Living Room'][0], Sofa)
        self.assertFalse(isinstance(homeobj['Bedroom'][0], Table))
    

    def test_count(self):
        "Tests the counter function"
        obsv_dict = counter(self.home)
        exp_Dict = {'Bookshelves':1, 'Tables':1, 'Beds':2, 'Sofas':2}
        self.assertEqual(exp_Dict, obsv_dict)



if __name__ == "__main__":
    unittest.main()
