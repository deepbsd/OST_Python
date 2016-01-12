#!/usr/bin/env python3

"""
arr.py:  Class-based array allowing tuple subscripting.
"""

import array as sys_array

class array:

    def __init__(self, M, N):
        "Create an M-element list of N-element row lists."
        self._data = sys_array.array("i", [0] * M * N)
        self._rows = M
        self._cols = N


    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col = self._validate_key(key)
        return self._data[row*self._cols+col]

    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col = self._validate_key(key)
        self._data[row*self._cols+col] = value

    def _validate_key(self, key):
        '''
        Validates a key against the array's shape, returning good tuples. 
        Raises KeyError on problems.
        '''
        row, col = key
        if (0 <= row < self._rows and 0 <= col < self._cols):
            return key
        raise KeyError("subscript out of range")



