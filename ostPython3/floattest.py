#!/usr/bin/env python3
"""
floattest.py: demonstrate use of floating-point values in files.
"""
import random, os, struct
#filename = r"v:\workspace\Python3_Lesson08\src\floatdata.bin"
filename = r"floatdata.bin"
rlist = [random.random() for i in range(10)]
f = open(filename, "wb")
f.write(struct.pack("=10d", *rlist))
f.close()
f = open(filename, "rb")
for i in range(10):
    s = f.read(8)
    x, = struct.unpack("=d", s)
    if x != rlist[i]:
        print(i, x, rlist[i], abs(x-rlist[i]))
    else:
        print(i, x, "values agree")
print(filename, os.stat(filename).st_size)
f.close()


