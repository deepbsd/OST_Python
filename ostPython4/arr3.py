#!/usr/bin/env python3

"""
arr3.py
"""

class array:

    def __init__(self, M, N, O):
        self._rows = []
        for _ in range(M):
            self._rows.append([0] * N * O)

    def __getitem__(self, key):
        row, col, depth = key
        return self._rows[row][col][depth]

    def __setitem__(self, key, value):
        row, col, depth = key
        self._rows[row][col][depth] = value

