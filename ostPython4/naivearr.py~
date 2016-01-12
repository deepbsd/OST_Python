#!/usr/bin/env python3
#
#
#        naivearr.py
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
naivearr.py:  Naive implementation of 3-D list-of-lists creation
"""

def array(M, N, O):
    "Create an M-element list of N-element and O-element row lists."
    rows = []
    for _ in range(M):
        cols = []
        for _ in range(N):
            depth = []
            for _ in range(O):
                depth.append(0)
            cols.append(depth)
        rows.append(cols)
    return rows



if __name__ == "__main__":
    print(array(4,4,4))

