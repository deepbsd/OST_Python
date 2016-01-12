#!/usr/bin/env python3

"""
thread2.py:  Use threading.Thread subclass to specify thread logic in run()
method.
"""
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, sleeptime, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        print("initializing", self.name)
        self.sleeptime = sleeptime

    def run(self):
        for i in range(self.sleeptime):
            for j in range(500000):
                k = j*j
            print(self.name, "finished pass", i)
        print(self.name, "finished after", self.sleeptime, "seconds")

R = 6

bgthreads = threading.active_count()

# adding bgthreads print stmt
print("There is(are) now {} background thread(s)....".format(bgthreads))

tt = [MyThread(i+1) for i in range(R)]
for t in tt:
    #adding print statement for calling run() method
    print("starting", t)
    t.start()

print("*** All {} threads started".format(threading.active_count()))

while threading.active_count() > bgthreads:
    time.sleep(2)
    print("tick... Now there are {} active threads".format(threading.active_count()))

print("All threads done")




