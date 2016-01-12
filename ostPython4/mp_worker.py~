#!/usr/bin/env python3
#
#
#         mp_worker.py
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
worker.py:  a sample worker process that receives input
through one queue and routes output through another.


Project:

Modify the control module from the final example of the lesson so that, 
instead of asking user for input, it generates a random string of alphabetic 
characters of length one thousand. Similarly modify the output routine 
to print out the length of the final string.

requires mp_control.py and mp_output.txt
"""

from multiprocessing import Process
import sys

class WorkerThread(Process):
    def __init__(self, iq, oq, *args, **kw):
        """Initialize process and save Queue references."""
        Process.__init__(self, *args, **kw)
        self.iq, self.oq = iq, oq

    def run(self):
        while True:
            work = self.iq.get()
            if work is None:
                self.oq.put(None)
                print("Worker", self.name, "done")
                self.iq.task_done()
                break
            i, c = work
            result = (i, self.process(c)) # this is the "work"
            self.oq.put(result)
            self.iq.task_done()
        sys.stdout.flush()

    def process(self, s):
        """This defines how the string is processed to produce a result."""
        return s.upper()


