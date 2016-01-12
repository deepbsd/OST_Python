#!/usr/bin/env python3

"""
Inheritance test program
"""

import unittest
from inhairitance import Child

class TestHair(unittest.TestCase):

    def test_hair(self):
        child = Child()
        hair = child.hair()
        self.assertNotEqual(hair, "red")
        self.assertNotEqual(hair, "brown")
        self.assertNotEqual(hair, "gray")
        self.assertEqual(hair, "bald")



if __name__ == "__main__":
    unittest.main()

