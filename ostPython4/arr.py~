#!/usr/bin/env python3

"""
arr.py:  Class-based dict array allowing tuple subscripting and sparse data.
"""


class array:

    def __init__(self, M, N):
        "Create an M-element list of N-element row lists."
        self._data = {}
        self._rows = M
        self._cols = N


    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col = self._validate_key(key)
        try:
            return self._data[row, col]
        except KeyError:
            return 0

    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col = self._validate_key(key)
        self._data[row, col] = value

    def _validate_key(self, key):
        '''
        Validates a key against the array's shape, returning good tuples. 
        Raises KeyError on problems.
        '''
        row, col = key
        if (0 <= row < self._rows and 0 <= col < self._cols):
            return key
        raise KeyError("subscript out of range")



