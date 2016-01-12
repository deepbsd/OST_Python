#!/usr/bin/env python3

"""
arr.py:  Class-based list of lists allowing tuple subscripting.
"""

class array:

    def __init__(self, M, N):
        "Create an M-element list of N-element row lists"
        self._rows = []
        for _ in range(M):
            self._rows.append([0] * N)


    def __getitem__(self, key):
        "Returns the appropriate element for a two-element subscript tuple."
        row, col = key
        return self._rows[row][col]

    def __setitem__(self, key, value):
        "Sets the appropriate element for a two-element subscript tuple."
        row, col = key
        self._rows[row][col] = value
