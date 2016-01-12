#!/usr/bin/env python3
#
#
#      test_subdictclass.py 
#
#    Lesson 6: Using Exceptions Wisely
#
#     by David S. Jackson
#          7/24/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
Tests the subdictclass.py program.
"""


from subdictclass import SubDict
import unittest


class TestSubDict(unittest.TestCase):

    def setUp(self):
        self.defkey = 'mykey'
        self.a = SubDict(self.defkey)
        self.a['one'] = 1
        self.a['two'] = 2

    def test_subdict(self):
        'Tests SubDict.__getitem__  . . . '
        self.assertEqual(self.a['one'], 1)
        self.assertEqual(self.a['two'], 2)

    def test_missingkey(self):
        "What happens when key doesn't exist? Shouldn't be KeyError!"
        boguskey = 'bogus_whatnot'
        #expected = 'default value'
        expected = self.a[self.defkey]
        self.assertEqual(self.a[boguskey], expected)




if __name__ == '__main__':
    unittest.main()
