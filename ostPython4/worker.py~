#!/usr/bin/env python3
#
#
#               worker.py
#
#    Lesson 11: More on Multi-Threading
#
#           by David S. Jackson
#               8/10/2015
#   
#     OST Python4: Advanced Python
#      for Pat Barton, Instructor
#
"""
worker.py: a sample worker thread that receives input through one Queue and
routes output through another.

includes: control.py and output.py    See control.py for project description

"""

from threading import Thread

class WorkerThread(Thread):
    def __init__(self, iq, oq, *args, **kw):
        """Initialize thread and save Queue references."""
        Thread.__init__(self, *args, **kw)
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
            result = (i, self.process(c))  # this is the 'work'
            self.oq.put(result)
            self.iq.task_done()
    def process(self, s):
        """This defines how the string is processed to produce a result"""
        # modified for project...
        return s.upper()



