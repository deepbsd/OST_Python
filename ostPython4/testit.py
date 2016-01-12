#!/usr/bin/env python3

from math import log
from timeit import Timer


def groffle_slow(mass, density):
    total = 0.0
    for i in range(10000):
        masslog = log(mass * density)
        total += masslog/(i+1)
    return total


def groffle_faster(mass, density):
    total = 0.0
    masslog = log(mass * density)
    return sum(map(masslog.__truediv__, range(1,10001)))



if __name__ == "__main__":

