#!/usr/bin/env python3


try:
    import cProfile as profile
except ImportError:
    import profile


def f1():
    for i in range(300):
        f2(); f3(); f5()

def f2():
    for i in range(300):
        f3()

def f3():
    for i in range(300):
        pass

def f4():
    for i in range(100):
        f5()

def f5():
    i = 0
    for j in range(100):
        i += j
    f6()

def f6():
    for i in range(100):
        f3()



profile.run("f1()", "profiledata")
