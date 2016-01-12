#!/usr/bin/env python3
#
#
#            control.py
#
#    Lesson 11: More on Multi-Threading
#
#          by David S. Jackson
#              8/10/2015
#   
#      OST Python4: Advanced Python
#        for Pat Barton, Instructor
#
"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.

project includes: output.py and worker.py

Project:

Modify the control module from the final example of the lesson so that,
instead of asking the user for input, it generates a random string of
alphabetic characters of length one thousand.  Similarly modify the output
routine to print only the length of the final string. Test the time it takes
the program to run. Make sure the workers report when done by printing to
console.

"""

from queue import Queue
from random import randint
import time

from output import OutThread
from worker import WorkerThread

# Added for project.  Used in computing program execution time
start_time = time.time()

WORKERS = 10

inq = Queue(maxsize=int(WORKERS*1.5))
outq = Queue(maxsize=int(WORKERS*1.5))

ot = OutThread(WORKERS, outq)
ot.start()

for i in range(WORKERS):
    w = WorkerThread(inq, outq)
    w.start()

#instring = input("Words of wisdom: ")

############################################################
##  Mods to program...
############################################################
# instring will now be a list of a thousand random characters
# add lowercase characters and uppercase characters to a list:
instring = ''
# chr(65-91) and chr(97-123) are upper-case and lower-case characters...
lista = [n for n in range(97, 123, 1)]
[lista.append(n) for n in range(65, 91, 1)]
# generate the string of 1000 characters...
for n in range(1000):
    c = randint(0, len(lista)-1)
    instring += chr(lista[c])




for work in enumerate(instring):
    inq.put(work)
for i in range(WORKERS):
    inq.put(None)
inq.join()

print("Control thread terminating...")
# added by project
end_time = time.time()
print("Total program time: {} seconds".format(end_time-start_time))



