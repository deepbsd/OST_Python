#!/usr/bin/env python3

"""
thread.py: Use threading.Thread subclass to specify thread logic in run()
method.
"""

import threading
import time

class MyThread(threading.Thread):

    def __init__(self, sleeptime, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        self.sleeptime = sleeptime
        # added printing of initializing self.name
        print("initializing: ", self.name)

    def run(self):
        print(self.name, "started")
        time.sleep(self.sleeptime)
        print(self.name, "finished after", self.sleeptime, "seconds")

# my addition to program
R = 6

bgthreads = threading.active_count()
print("starting bgthreads count is: ", bgthreads)
tt = [MyThread(i+1) for i in range(R)]
for t in tt:
    # added print name
    print("name:", t)
    t.start()

# changed to include count of active threads...
print("*** {} total threads started...".format(threading.active_count()))


while threading.active_count() > bgthreads:
    time.sleep(2)
    # added active threads count
    print("tick...", "Active threads:", threading.active_count())

print("All threads done")





