#!/usr/bin/env python3

"""
Created 4/11/2015
@author Dave Jackson
lifted from OST Python3 text
by Steve Holden (8-29-2010)

Tests the zip_errors() function
from the zipcheck module
"""

import unittest
from zipcheck import zip_errors

class Test(unittest.TestCase):

    def test_zip_errors(self):
        "Tests ensuring errors in data cause validation failures."
        self.assertIsNotNone(zip_errors("1234"), "Accepting length 4")
        self.assertIsNotNone(zip_errors("12345-678"), "Accepting length 9")
        self.assertIsNotNone(zip_errors("1234e"), "Accepting alphabetic 5")
        self.assertIsNotNone(zip_errors("12345-678Y"), "Accepting Alphabetic 5+4") 
        self.assertIsNotNone(zip_errors("12345/6789"), "Accepting non-hyphen")


    def test_zip_successes(self):
        "Tests ensuring that valid data passes."
        self.assertIsNone(zip_errors("12345"), "Not accepting 5-digit zips")
        self.assertIsNone(zip_errors("12345-6789"), "Not accepting 9-digit zips")



if __name__ == "__main__":
    #import sys; sys.argv = ['', 'Test.test_zip_errors']
    unittest.main()




