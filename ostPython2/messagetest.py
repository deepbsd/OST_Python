#!/usr/local/bin/python3
# 
#  Quality program copied from
#  OST Python2 Lesson 3 Class
#    typed by David S Jackson
#     Instructor: Pat Barton
#
"""
Demonstrate a message formulated by the unittest system.
"""

import unittest

class DemoCase(unittest.TestCase):
    def testMessage1(self):
        self.assertEqual([1,2,3,4], [1,2,[3,4]])

if __name__ == "__main__":
    unittest.main()


