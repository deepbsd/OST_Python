#!/usr/bin/env python3

"""
arr.py:  Class-based dict array allowing tuple subscripting and sparse data.
"""


class array:

    def __init__(self, M, N, O):
        "Create an M-element list of N-element row lists."
        self._data = {}
        self._rows = M
        self._cols = N
        self._depth = O


    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col, depth = self._validate_key(key)
        try:
            return self._data[row, col, depth]
        except KeyError:
            return 0

    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col, depth = self._validate_key(key)
        self._data[row, col, depth] = value

    def _validate_key(self, key):
        '''
        Validates a key against the array's shape, returning good tuples. 
        Raises KeyError on problems.
        '''
        row, col, depth = key
        if (0 <= row < self._rows and 0 <= col < self._cols and 0 <= depth < self._depth):
            return key
        raise KeyError("subscript out of range")



