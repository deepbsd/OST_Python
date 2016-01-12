#!/usr/bin/env python3

import mmap


#count = 1024 * 1024 * 10
count = 1

with open('test.out', 'wb') as f:
    for n in range(count):
        f.write(b'Hello Python!\n')



with open('test.out', 'r+b') as f:
    fmap = mmap.mmap(f.fileno(), 0)
    print(fmap.readline())
    print(fmap[:5])
    print(fmap.tell())
    fmap[6:] = b' world!\n'
    fmap.seek(0)
    print(fmap.readline())
    fmap.close()



