#!/usr/bin/env python3

import itertools

s1 = (1,3,5,7,11)
s2 = ['one', 'two', 'three', 'four']

def sqq(n):
    for i in range(n):
        yield i*i

s3 = sqq(10)

input = itertools.chain(s1, s2, s3)

myobj = input
print(type(myobj))
#mylst = list(myobj)
#print(mylst)

print(list(itertools.islice(input, 2, 7, 2)))

print(list(itertools.islice(input, 3)))


