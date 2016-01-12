#!/usr/bin/env python3
#
#
#    test_property_address.py
#
#    Lesson 11: A First Look
#          at Logging
#
#     by David S. Jackson
#          5/25/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
This test module evaluates the Addreses class and the two new
Exception classes: StateError and ZipCodeError.  These all are part of the 
property_address module.  This test module was specified in the project
description from Oreilly.

This utility is used for both Chapter 10 and Chapter 11.  For chapter 11, 
a logging utility is started just before the main() module of unittest.
"""

import unittest
from property_address import *

class TestAddresses(unittest.TestCase):

    def setUp(self): 
        # test two formats of State and Zip:  'ABC' state and '12345-1234' zip
        # formats

        #self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VA', zip_code='12345')
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VAZ', zip_code='12345-1234')

    def test_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')  

    def test_state(self): 
        self.assertEqual(self.home.state, 'VAZ') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')  
        self.home.state = 'COL' 
        self.assertEqual(self.home.state, 'COL')  

    def test_zip_code(self): 
        self.assertEqual(self.home.zip_code, '12345-1234') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '123456') 
        self.home.zip_code = '54321-4321' 
        self.assertEqual(self.home.zip_code, '54321-4321') 


if __name__ == "__main__":
    # This is the only thing added to the test...
    start_logging(level='info')
    unittest.main()



