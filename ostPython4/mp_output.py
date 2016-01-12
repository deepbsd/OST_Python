#!/usr/bin/env python3
#
#
#         mp_output.py
#
#    Lesson 12: Multi-Processing
#
#     by David S. Jackson
#          8/12/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
output.py: The output process for the miniature framework.

Project:

Modify the control module from the final example of the lesson so that, 
instead of asking user for input, it generates a random string of alphabetic 
characters of length one thousand. Similarly modify the output routine 
to print out the length of the final string.

requires mp_control.py mp_worker.py
"""


import multiprocessing
import sys


identity = lambda x: x


class OutThread(multiprocessing.Process):
    def __init__(self, N, q, sorting=True, *args, **kw):
        """Initialize process and save queue reference."""
        multiprocessing.Process.__init__(self, *args, **kw)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []

    def run(self):
        """Extract itmes and print until all done."""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # This is a real output packet
                self.output.append(p)

        ###############################
        #### Changed for Project ######
        ###############################
        #print("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output)))
        print("Length of Final String {} chars".format(len(self.output)))
        print("Output process terminating")
        sys.stdout.flush()


