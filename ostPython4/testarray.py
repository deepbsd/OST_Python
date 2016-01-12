#!/usr/bin/env python3

"""
testarray.py: Test list-of-list based array implementations using tuple
subscripting.
"""

import unittest
import arr_single_list as arr

class TestArray(unittest.TestCase):

    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
                for j in range(N):
                    #self.assertEqual(a[i][j], 0)
                    self.assertEqual(a[i, j], 0)

    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
                #a[i][i] = 1
                a[i, i] = 1
            for i in range(N):
                for j in range(N):
                    #self.assertEqual(a[i][j], i==j) 
                    self.assertEqual(a[i, j], i==j)

    def test_one_cell(self):
        N = 10 
        a = arr.array(N,N)
        a[2,3] = 1
        for i in range(N):
            for j in range(N):
                if i==2 and j==3:
                    self.assertEqual(a[i,j], 1)
                else:
                    self.assertEqual(a[i,j], 0)


    def _index(self, a, r, c):
        return a[r, c]

    def test_key_validity(self):
        a = arr.array(10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1)
        self.assertRaises(KeyError, self._index, a, 1, 10)


if __name__ == "__main__":
    unittest.main()



