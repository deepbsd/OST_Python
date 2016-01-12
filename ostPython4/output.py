#!/usr/bin/env python3
#
#
#               output.py
#
#    Lesson 11: More on Multi-Threading
#
#           by David S. Jackson
#               8/10/2015
#   
#      OST Python4: Advanced Python
#       for Pat Barton, Instructor
#
"""
project includes:  control.py and worker.py.  See control.py for project
description.

output.py:  The output thread for the miniature framework.
"""
import threading

identity = lambda x: x

class OutThread(threading.Thread):
    def __init__(self, N, q, sorting=True, *args, **kw):
        """Initialize thread and save queue reference."""
        threading.Thread.__init__(self, *args, **kw)
        self.queue = q
        self.workers = N
        self.sorting = sorting
        self.output = []
    def run(self):
        """Extract items from the output queue and print until all done"""
        while self.workers:
            p = self.queue.get()
            if p is None:
                self.workers -= 1
            else:
                # This is a real output packet
                self.output.append(p)
        #print("".join(c for (i, c) in (sorted if self.sorting else identity)(self.output)))
        # Changed for project
        print("Length of Final String: {} chars".format(len(self.output)))
        print("Output thread terminating")


