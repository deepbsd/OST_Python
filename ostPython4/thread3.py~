#!/usr/bin/env python3

"""
#thread3.py: Use threading.Lock to ensure threads run sequentially.
thread3.py: Without threading.Lock, threads sleep in parallel.
"""

import threading
import time

R = 10

class MyThread(threading.Thread):
    def __init__(self, lock, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        self.lock = lock
    def run(self):
        for i in range(R):
            #self.lock.acquire()
            time.sleep(0.1)
            #self.lock.release()
        self.lock.acquire()
        print(self.name, "finished")
        self.lock.release()

lock = threading.Lock()
bgthreads = threading.active_count()
tt = [MyThread(lock) for i in range(R)]
for t in tt:
    t.start()
print("Threads started")
while threading.active_count() > bgthreads:
    time.sleep(2)
    print("tick")
print("All threads done")


