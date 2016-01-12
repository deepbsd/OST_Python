#!/usr/bin/env python3
#
#
#      lesson10_proj.py
#
#    Lesson 10: Multi-Threading
#
#     by David S. Jackson
#          8/5/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
Project:

    Write a program that determines whether changing the current directory
    using os.chdir in one thread changes the current directory for:

    * a thread that already existed before the call to os.chdir.
    * a thread that is created after the call to os.chdir

    State your conclusions, based on experiment, in your comments.


Author observations:

    When the join() function is used and thread1 finishes before the start of
    thread2, then thread1 finishes in the same working directory where it
    started.

    However, if the join() function is NOT used, then thread1 finishes in the
    same directory as thread2.

    Conclusion:  It doesn't matter whether there's a long delay for thread1.
    What matters is whether join() is used or not.  For thread1 to finish in
    the directory where it started, join() must be used.  Otherwise thread1
    will finish in the same directory where thread2 finishes.
    
"""

import os

import threading
import time

#################
# START UP VALUES:
#################
dest_dir = '/home/dsj'
#dest_dir = '../..'  # for ellipse environment on windoze...
delay = 5
join = True

# Initialize a class for threads...

class MyThread(threading.Thread):

    def __init__(self, curdir, *args, **kw):
        "self.curdir should start from os.getcwd() at init of thread"
        threading.Thread.__init__(self, *args, **kw)
        self.curdir = curdir

    def run(self):
        """ Prints startup dir, then prints completion directory. 'delay' is global
        variable."""
        print(self.name, "started in {}, sleeping for {} seconds...".format(self.curdir, delay))
        time.sleep(delay)
        self.nowdir = os.getcwd()
        print(self.name, "finished in ", self.nowdir)



def thread1():
    "If join() is true, use join() method, else don't. Start in CWD."
    if join:
        t1 = MyThread(os.getcwd())
        t1.start()
        t1.join()
    else:
        t1 = MyThread(os.getcwd())
        t1.start()


def thread2():
    "Like thread1, start in current working directory"
    t2 = MyThread(os.getcwd())
    t2.start()


if __name__ == '__main__':
    thread1()
    os.chdir(dest_dir)
    thread2()
    print("Join value is: ", join)


