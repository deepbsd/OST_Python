#!/usr/bin/env python3

'''
Demonstrate how to make instances callable.
'''

class funclike:
    def __call__(self, *args, **kwargs):
        print("Args are:", args)
        print("Kwargs are:", kwargs)

f = funclike()
f(1, 2, 3, this="one", that="the other")
