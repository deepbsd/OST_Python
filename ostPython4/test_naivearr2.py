#!/usr/bin/env python3
#
#
#       test_naivearr2.py
#
#    Lesson 2: Data Structures
#
#     by David S. Jackson
#          7/7/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
Test list-of-list array implementation using tuple subscripts"
"""

import unittest
import naivearr2 as arr    # list-based solution   
#import arr_dict_array as arr    # dict-based solution  it works!


class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(6):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        #print("N={}, i={}, j={}, k={}".format(N, i, j, k))
                        self.assertEqual(a[i, j, k], 0)

    def test_identity(self):
        for N in range(6):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
                #print("a[{},{},{}] ".format(i, i, i))
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        if i==j==k:
                        #self.assertEqual(a[i,j,k], i==j==k)
                            #print("***A[{},{},{}]".format(i, j, k))
                            self.assertEqual(a[i, j, k], 1)
                        #if not i==j==k and a[i,j,k] == 1:
                        else:
                            #print("Dammit!  A[{},{},{}] == 1".format(i, j, k))
                            self.assertEqual(a[i,j,k], 0)

    def test_one_cell(self):
        N = 10
        a = arr.array(N,N,N)
        a[2,3,1] = 1
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i==2 and j==3 and k==1:
                        self.assertEqual(a[i,j,k], 1)
                    else:
                        self.assertEqual(a[i,j,k], 0)

    def _index(self, a, r, c, d):
        return a[r, c, d]

    def test_key_validity(self):
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1, 10)
        self.assertRaises(KeyError, self._index, a, 1, -1, -10)
        self.assertRaises(KeyError, self._index, a, 1, 10, -1)



if __name__ == "__main__":
    unittest.main()

