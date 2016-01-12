#!/usr/bin/env python3


def addarg(a):
    """Returns a decorator that adds 'a' to the beginning of the *args for the
    calling function"""
    #print(a)
    def decorator(f):
        "decorator containing a wrapper function that adds the 'a' argument"
        def wrapper(*args, **kw):
            "Counts every call as being of the given type."
            myarg = a
            return f(myarg, *args, **kw)
        return wrapper
    return decorator

@addarg(1)
def f1(*args, **kw):
    print("f1 called with:", args, kw)

@addarg(2)
def f2(*args, **kw):
    print("f2 called with:", args, kw)

@addarg(3)
def f3(*args, **kw):
    print("f3 called with:", args, kw)

@addarg(4)
def f4(*args, **kw):
    print("f4 called with:", args, kw)

for i in range(10):
    f1(1, 2, a=1)
    f2(2, 3, b=2)
    f3(3, 4, c=3)
    f4("child")


#for k in sorted(counts.keys()):
#    print(k, ":", counts[k])
