#!/usr/bin/env python3
#
#
#        mmaptimer.py
#
#    Lesson 15: Memory Mapped 
#            Files
#
#     by David S. Jackson
#          8/21/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
'''
Project:  

Write a program that creates a ten-megabyte data file in two different ways,
and time each method. The first technique should create a memory-mapped file
and write the data by setting one chunk at a time using successively higher
indexes. The second technique should create an empty binary file and repeatedly
use the write() method to write a chunk of data. Show how the timings vary with
the size of the chunk.

Student Note:

    make_binf() uses the write() method to write a 10MB file out using a static
    CHUNKSIZE value.  It gets that value by calling get_chunksize() with a
    value for 'n', which doesn't change.

    make_mapf() on the other hand, calls get_chunksize() with increasing values
    for 'n'.  

    Both programs use a while loop that checks the output file size against the
    10MB limit and exits when that threshold is exceeded.  

    If I were to write a test program for this module, I would alter the
    functions so they accepted a CHUNKSIZE value as an argument.  But since we
    were looking at timings between the two processes, I wasn't sure how a test
    suite would be more informative than the output the this module itself.

    Timings: The write() method wins hands down.  It's much faster, at least in
    this case.  Under all attempted scenarios, the write() method still wins.
    Sometimes it wins profoundly, and sometimes just soundly.  As the CHUNKSIZE
    value changes for the mmap() method, there does *not* seem to be much
    correlation to the speed of the operation.  As you can see in the output,
    CHUNKSIZE does not appear to influence the speed of in-memory operations
    very much.  On the other hand, CHUNKSIZE *does* seem to influence the
    write() method speed.  The write() method speed seems fastest while
    CHUNKSIZEs are small.  That's my first hypoethesis anyway.  That would
    require further testing, but these are my results for now.

    Further Note: This all changes once we get onto the OST network!!!  That
    machine has 10 processors and 24GB of RAM!  My programs FLEW on that
    machine!  Oh, and mmap() won!  f.write() wasn't too far behind.  But this
    was a totally different scenario than on my home dev machine!

'''


import struct, mmap, os, time, sys

MAPFILE = "mmappedfile"
BINFILE = "binfile"

CHUNKSIZE = 1024
MB = 10
KB = 1024
FILESIZE = CHUNKSIZE * MB * KB

def make_binf():
    """Make the finary file with a static CHUNKSIZE using the built-in write()
    method"""
    n = 1
    CHUNKSIZE = get_chunksize(n)
    f = open(BINFILE, 'wb')
    while os.path.getsize(BINFILE) <= FILESIZE:
        f.write(CHUNKSIZE*b'\0')
    f.close

def get_chunksize(n):
    "Return the chunksize upon request.  N is a multiplier parameter."
    CHUNKSIZE = 1024
    return CHUNKSIZE*(n*100)
    #return CHUNKSIZE*n

def make_mapf():
    """This is the mmap() method that uses increasingly larger CHUNKSIZE values
    to write from memory to the file.  It uses the mmap.resize() method to
    work. It prints a table of CHUNKSIZE values and their respective completion
    times.  Since most of this method happens in-memory, speeds are not greatly
    affected by CHUNKSIZE values."""
    n = 1
    CHUNKSIZE = get_chunksize(n)
    chunk_times = {}
    f = open(MAPFILE, 'w+b')
    f.write(CHUNKSIZE*b'\0')
    f.close
    f = open(MAPFILE, 'r+b')
    mapf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    while mapf.size() <= FILESIZE:
        start_t = time.time()
        size = mapf.size()
        oldsize = size+1
        CHUNKSIZE = get_chunksize(n)
        newsize = size+CHUNKSIZE+1
        mapf.resize(newsize)
        mapf[oldsize:newsize] = CHUNKSIZE*b'\0'
        n += 1
        mapf.flush()
        end_t = time.time()
        total_t = end_t - start_t
        chunk_times[CHUNKSIZE] = total_t
    mapf.close()
    sys.stdout.flush()
    f.close()
    print("Chunksize       Time")
    print("=========       =====")
    for k in sorted(chunk_times.keys()):
        print("{0} Bytes    {1:.5f} Sec ".format(k, chunk_times[k]))



if __name__ == "__main__":
    # Start for the MMAPPEDFILE
    mf_start_time = time.time()
    make_mapf()
    mf_end_time = time.time()
    fsize = os.path.getsize(MAPFILE)
    print('\nTotal time for mmap file = {} seconds.'.format(mf_end_time - mf_start_time), " \nTotal Size of mmap file: {}KB".format(round(fsize/1024, 2)))

    # Start for the BINFILE
    bf_start_time = time.time()
    make_binf()
    bf_end_time = time.time()
    binfile_size = os.path.getsize(BINFILE)
    print('\nTotal time for write() binfile = {} seconds.'.format(bf_end_time -
        bf_start_time), "\nTotal size for binfile = {}KB\n".format(round(binfile_size/1024, 2)))
    #  Can comment this out if desired; I wanted to clean up afterwards...
    os.unlink(MAPFILE)
    os.unlink(BINFILE)

