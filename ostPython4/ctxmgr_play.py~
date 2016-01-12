#!/usr/bin/env python3

"""
playing around with context managers
"""
from contextlib import contextmanager

class ctx_mgr:
    def __init__(self, raising=True):
        print("Created new context manager object", id(self))
        self.raising = raising

    def __enter__(self):
        print("__enter__ called")
        cm = object()
        print("__enter__ returning object id:", id(cm))
        return cm
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called")
        if exc_type:
            print("An exception occurred")
            if self.raising:
                print("Re-raising exception")
            return not self.raising

@contextmanager
def ctx_man(raising=False):
    try:
        cm = object()
        print("Context manager returns:", id(cm))
        yield cm
        print("With concluded normally")
    except Exception as e:
        print("Exception", e, "raised")
        if raising:
            print("Re-raising exception")
            raise



if __name__ == "__main__":

    with ctx_mgr(raising=True) as cm:
        print("cm ID:", id(cm))
    
    #with ctx_mgr(raising=True) as cm:
    #    3/0

    #with ctx_man() as cm:
    #    print("cm from __enter__():", id(cm))

    #with ctx_man(True) as cm:
    #    3/0







