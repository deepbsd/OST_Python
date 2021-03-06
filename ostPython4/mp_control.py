#!/usr/bin/env python3
#
#
#        mp_control.py
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
Project:

Modify the control module from the final example of the lesson so that, 
instead of asking user for input, it generates a random string of alphabetic 
characters of length one thousand. Similarly modify the output routine 
to print out the length of the final string.

mp_control.py:  Creates queues, starts output and worker processes,
and pushes inputs into the input queue.

requires mp_output.py and mp_worker.py  Also needed to add randint() to mix.
"""

from multiprocessing import Queue, JoinableQueue
from mp_output import OutThread
from mp_worker import WorkerThread

from random import randint



if __name__ == '__main__':
    WORKERS = 10

    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))

    ot = OutThread(WORKERS, outq, sorting=True)
    ot.start()

    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()

    #instring = input("Words of wisdom: ")



    ##########################
    #####  Changed for Project
    ##########################
    # Changed per project: instring is a generated list of alpha characters.
    lista = [n for n in range(97, 123, 1)]
    [lista.append(n) for n in range(65, 91, 1)]
    instring = ''
    for n in range(1000):
        c = randint(0, len(lista)-1)
        instring += chr(lista[c])



    # feed the process pool with work units
    for work in enumerate(instring):
        inq.put(work)
    # terminate the process pool
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating")





