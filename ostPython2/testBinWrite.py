#!/usr/local/bin/python3

""" Tries to write a file of exactly 1000000 bytes in binary
"""

import os
import struct

"""
packed = struct.pack('>i4sh', 7, b'spam', 8)
outfile = open("binout.bin", 'wb')
for num in (range(0, 100000)):
        outfile.write(packed)    # should be 10 bytes long
outfile.close()
info = os.stat(r"binout.bin")
size = info.st_size
print("Outfile created: {} bytes long".format(size))
"""

fn = r"binout.bin"
file_handle = open(fn, 'wb')
intended_size = 1000000
file_handle.write(bytes(intended_size))
file_handle.close()
actual_size = os.stat(fn).st_size
print("Outfile created!  Intended: {} bytes; Actual: {} bytes".format(intended_size, actual_size))

"""
self.assertTrue(actual_size==intended_size)
self.assertEqual(actual_size, intended_size + 1, "Wrong! Looking for {}".format(intended_size))
"""



