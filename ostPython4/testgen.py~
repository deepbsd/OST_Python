#!/usr/bin/env python3

import math

p = math.pi
#print(p)

crazynum = 1/3
crazy_len = len(str(crazynum))

def givenum():
    for n in str(crazynum):
        yield n


def givepi():
    for n in str(p):
        yield n

if __name__ == "__main__":
    #numobj = givepi()
    numobj = givenum()
    while True:
        try:
            print(next(numobj), end="")
        except StopIteration:
            print("\n . . . {} places of accuracy! That's good enough for now folks!".format(crazy_len))
            break
