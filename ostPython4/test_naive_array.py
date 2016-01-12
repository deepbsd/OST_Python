#!/usr/bin/env python3
#
#
#      test_naive_array.py
#
#    Lesson 2: Data Structures
#
#     by David S. Jackson
#          6/22/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
test_naive_array.py: test list of 3-D based array implementations.
"""

import unittest
import naivearr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = naivearr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i][j][k], 0)


    def test_identity(self):
        for N in range(4):
            a = naivearr.array(N, N, N)
            for i in range(N):
                a[i][i][i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i][j][k], i==j==k)



if __name__ == "__main__":
    unittest.main()

