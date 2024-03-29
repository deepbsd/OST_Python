#!/usr/bin/env python3

"""
naievearr3.py:  Naive implementation of 3-D array using lists and tuple
subscripts
"""

import array as sys_array

class array:

    def __init__(self, M, N, O):
        "Create 3-D array of lists"
        self._data = sys_array.array("i", [0] * M * N * O)
        self._rows = M
        self._cols = N
        self._depth = O

    def __getitem__(self, key):
        "returns the appropriate element for a three-element subscript tuple."
        row, col, depth = self._validate_key(key)
        # debugging print statement...
        #print("get ", key, ": ", self._data[row*self._cols+col*self._depth+depth])
        #return self._data[row*self._cols+col*self._depth+depth]
        return self._data[row*self._cols*self._depth+col*self._depth+depth]

    def __setitem__(self, key, value):
        "sets the appropriate element for a three-element subscript tuble."
        row, col, depth = self._validate_key(key)
        # debugging pring statement...
        #print("set ", key, ": ", self._data[row*self._cols+col*self._depth+depth], "->", value)
        #print("set ", key, ": ", self._data[row*self._cols+col*self._depth+depth], "->", value)
        self._data[row*self._cols*self._depth+col*self._depth+depth] = value

    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        row, col, depth = key
        if (0 <= row < self._rows and 0 <= col < self._cols and 0 <= depth < self._depth):
            #print("validate key: {}".format(key))
            return key
        raise KeyError("subscript out of range")



if __name__ == "__main__":
    for N in range(5):
        print("===Array is {}x{}===".format(N,N))
        a = array(N,N,N)
        for i in range(N):
            a[i,i,i] = 1
        for i in range(N):
            print("\nrow={}".format(i))
            for j in range(N):
                for k in range(N):
                    if i==j==k and a[i,j,k] == 1:
                        print(" \nYay! ***a[{},{},{}] = 1 *** ".format(i,j,k))
                    if a[i,j,k] == 1 and not i==j==k:
                        print(" \n+++ Crap!!! a[{},{},{}] = 1  +++ ".format(i,j,k))
        
