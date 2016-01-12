#!/usr/bin/env python3

'''
Kirby's solution to wireshark assignment...
'''

import struct

filename = "wireshark.bin"
f = open(filename, "rb")
f.read(24)
cnt = 1
while f:
    pack_header = f.read(16)
    if not pack_header:
        break
    (ts_sec, ts_usec, incl_len, orig_len) = struct.unpack('=LLLL', pack_header) 
    f.read(incl_len)
    print("Packet {0}: Time in [sec]={1}, + [msec]={2}".format(cnt,ts_sec,ts_usec))
    cnt += 1
