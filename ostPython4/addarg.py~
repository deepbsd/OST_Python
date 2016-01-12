#!/usr/bin/env python3
#
#
#        addarg.py
#
#    Lesson 7: Advanced Uses of Decorators
#
#     by David S. Jackson
#          7/29/2015
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#
"""
Project: 

Write a decorator function addarg() that takes an argument and adds
that argument as the first argument to all calls to decorated functions.  So if
you wrote:

    @addarg(1)
    def prargs(*args):
      return args

    prargs(2, 3)
    prargs("child")

    the output would be:
    (1, 2, 3)
    (1, 'child')

Write a test program to verify the decorator's operation.

Note: it's possible the wrapped function will have keyword arguments and these
should be respected.
"""

from functools import wraps

def addarg(a):
    """Returns a decorator that adds 'a' to the beginning of the *args for the
    calling function"""
    #print(a)
    def decorator(f):
        "decorator containing a wrapper function that adds the 'a' argument"
        @wraps(f)
        def wrapper(*args, **kw):
            "Counts every call as being of the given type."
            myarg = a
            return f(myarg, *args, **kw)
        return wrapper
    return decorator

@addarg('f1')
def f1(*args, **kw):
    print("f1 called with:", args, kw)

@addarg('f2')
def f2(*args, **kw):
    print("f2 called with:", args, kw)

@addarg('f3')
def f3(*args, **kw):
    print("f3 called with:", args, kw)

@addarg('f4')
def f4(*args, **kw):
    print("f4 called with:", args, kw)

if __name__ == "__main__":
    for i in range(10):
        f1(1, 2, a=1)
        f2(2, 3, b=2)
        f3(3, 4, c=3)
        f4("child")


#for k in sorted(counts.keys()):
#    print(k, ":", counts[k])
