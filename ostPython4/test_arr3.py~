#!/usr/bin/env python3

"""
test_arr3.py
"""

import unittest
#import arr3 as arr
#import naivearr2 as arr
import arr_dict_array as arr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N,N,N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i,j,k], 0)

    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i,i,i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i,j,k], i==j==k)

    def test_one_cell(self):
        N = 10
        for N in range(N):
            a = arr.array(N,N,N)
        a[2,3,4] = 1
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i==2 and j==3 and k==4:
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
