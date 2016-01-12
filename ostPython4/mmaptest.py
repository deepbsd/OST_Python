#!/usr/bin/env python3

import os
import mmap

with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")
    #f.write(b"Hello Python!")
    f.close()

'''
with open("hello.txt", "r+b") as f:
    # size 0 means the whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())
    # read content via slice notation
    print(mm[:5])    # prints b"Hello"
    # update content using slice notation
    # note that new content must have same size limit
    mm[6:] = b"World! \n"
    # and read again using standard file methods
    mm.seek(0)
    print(mm.readline())   # prints b"Hello  world!\n"
    # close the map
    mm.close()
'''


R = 3
text = 'abcd'
textlen = len(text)
with open("hello.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    for n in range(R):
        start = n*textlen
        mm[start:start+textlen] = b'abcd'
        mm.seek(0)
        mm.flush()
        print(mm.readline())
mm.seek(0)
print("file1st: ", mm.readline(), mm.readline())
mm.close


R = 1024000*2
text = 'efgh'
textlen = len(text)

with open("hello.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    for n in range(R):
        size = mm.size()
        #print("size:", size, "textlen:", textlen)
        #newsize = size+textlen
        newsize = size+textlen+1
        mm.resize(newsize)
        #mm[size+1:newsize] = b'efgh'
        mm[size+1:newsize] = b'efgh'
        #print(mm.readline())
        #print("slice[0:14]:", mm[0:14])
        #print("slice[15:20]:", mm[15:20])
        #print("size:", size, "textlen:", textlen)
    mm.flush()
    mm.close()
    #mm.seek(0)
    #print(mm.readline(), mm.readline())


'''
R = 4
with open("hello.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    size = mm.size()
    print("file size: ", size)
    newsize = size+6
    mm.resize(newsize)
    mm.seek(12)
    print("at 12: ", mm.read_byte())
    print(mm.size(), mm[14], mm[18])
    #mm.move(19,14,1)
    mm.seek(13)
    mm.write(b' ')
    
    mm[size+1:newsize] = b'efgh\n'
    print("cursor position: ", mm.tell())
    print(mm.readline())
    #print(mm.readline())
    #print(mm.size())
    mm.seek(0)
    #print(mm[size+1:newsize])
    print("slice[0-14]: ", mm[0:14])
    print("slice[15-20]: ", mm[15:20])
    mm.seek(0)
    print('file2nd: ', "line 1: ", mm.readline(), "line 2: ", mm.readline())
    #print('file2nd: ', mm.readline())
    mm.flush()
    mm.close
    f.close()
'''

    
