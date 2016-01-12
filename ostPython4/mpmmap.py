#!/usr/bin/env python3

"""
mpmmap.py: use memory-mapped file as an interprocess communication area 
to support multi-processed applications.

"""

import struct
import mmap
import multiprocessing as mp
import os
import time
import sys


FILENAME = "mappedfile"
SLOTFMT = b"B7s3d"
SLOTSIZE = struct.calcsize(SLOTFMT)
SLOTS = 6  # Number of subprocesses
EMPTY = 255
TERM = 254

def unpackslot(byte_data):
    """Return slot data as (slot#, string, float, float, float)."""
    return struct.unpack(SLOTFMT, byte_data)

def packslot(slot, s, f1, f2, f3):
    """Generate slot string from individual data elements."""
    return struct.pack(SLOTFMT, slot, s, f1, f2, f3)

def run(slot):
    """Implements the independent processes that will consume the data."""
    offset = SLOTSIZE*slot
    print("Process", slot, "running")
    sys.stdout.flush()
    f = open(FILENAME, "r+b")
    mapf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    while True:
        while mapf[offset] == EMPTY:
            time.sleep(0.01)
        if mapf[offset] == TERM:
            print("Process", slot, "done")
            sys.stdout.flush()
            mapf.close()
            return
        x, s, f1, f2, f3 = unpackslot(mapf[offset:offset+SLOTSIZE])
        print(x, slot, ":", s, f1*f2*f3)
        sys.stdout.flush()
        mapf[offset] = EMPTY

def numbers():
    """Generator: 0.01, 0.02, 0.03, 0.04, 0.05, ..."""
    i = 1
    while True:
        yield i/100.0
        i += 1

if __name__ == "__main__":
    f = open(FILENAME, "wb")
    f.write(SLOTSIZE*SLOTS*b'\0')
    f.close()
    f = open(FILENAME, "r+b")
    mapf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

    ptbl = []
    for slot in range(SLOTS):
        offset = slot*SLOTSIZE
        mapf[offset] = EMPTY
        p = mp.Process(target=run, args=(slot, ))
        ptbl.append(p)
        print("Starting", p)
        p.start()

    numseq = numbers()
    b = next(numseq)
    c = next(numseq)
    for i in range(4):
        for slot in range(SLOTS):
            a, b, c = b, c, next(numseq)
            offset = slot*SLOTSIZE
            while mapf[offset] != EMPTY:
                time.sleep(0.01)
            mapf[offset+1:offset+SLOTSIZE] = packslot(slot, b"********", a, b, c)[1:]
            mapf[offset] = slot

    for slot in range(SLOTS):
        offset = SLOTSIZE*slot
        while mapf[offset] != EMPTY:
            time.sleep(0.01)
        mapf[offset] = TERM

    for p in ptbl:
        p.join()

    mapf.close()
    print(f.read())
    sys.stdout.flush()
    f.close()
    os.unlink(FILENAME)


