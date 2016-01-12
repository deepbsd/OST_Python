#!/usr/bin/env python3

"""
#thread.py: demonstrate creation and parallel execution of threads.
#thread.py: demonstrate simple monitoring of execution of threads.
thread.py: demonstrate thread monitoring by awaiting termination.
"""

import threading
import time

def run(i, name):
    """Sleep for a given number of seconds, report and terminate."""
    # more obvious when each thread starts now...
    print(name, "started...")
    time.sleep(i)
    print(name, "finished after", i, "seconds")

threads = []

R = 10
# changed count to 10 so I could watch longer...
for i in range(R):
    # changed 'i' argument to '6-i'
    t = threading.Thread(target=run, args=(R-i, "Thread-"+str(i)))
    print("Call to start Thread-"+str(i),"...")
    t.start()
    threads.append((i, t))

print("All threads started!")

#while threading.active_count() > bgthreads:
#    print("Tick . . . ")
#    time.sleep(2)

for i, t in threads:
    t.join()
    print("Thread", i, "done")

print("All threads done")



