#!/usr/bin/env python3

from random import random
from timeit import timeit

for i in (10000, 100000, 1000000, 10000000, 20000000, 50000000):
    lst = [random() for j in range(i)]
    print("Length", i)
    print(timeit("sum(x+1 for x in lst)", "from __main__ import lst", number=1))
    print(timeit("sum([x+1 for x in lst])", "from __main__ import lst", number=1))




