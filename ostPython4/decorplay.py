#!/usr/bin/env python3


'''
# a function as a decorator
def one(func):
    def two(*args, **kw):
        print('Entering', func.__name__)
        b_args = []
        for a in args:
            b_args.append("Hi "+a.upper())
        result = func(*b_args, **kw)
        print('Leaving', func.__name__)
        return result
    return two
'''


# using a class as a decorator...
class one:
    def __init__(self, f):
        "__init__ records the passed function for later use in __call__"
        self.__doc__ = f.__doc__
        self.__name__ = f.__name__
        self.f = f

    def __call__(self, *args, **kw):
        "Prints a trace line before calling the wrapped function."
        print("Called", self.f.__name__, "from", type(self))
        b_args = []
        for a in args:
            b_args.append(a.upper()+" (a 'decorated' cutie pie)")
        return self.f(*b_args, **kw)



# trace function from early in lesson
def trace(f):
    "Decorate a function to print a message before and after execution."
    def traced(*args, **kw):
        "Print message before and after a function call."
        print("Entering", f.__name__)
        result = f(*args, **kw)
        print("Leaving", f.__name__)
        return result
    return traced

def callable(o):
    return hasattr(o, "__call__")

def mtrace(cls):
    for key, val in cls.__dict__.items():
        if key.startswith("__") and key.endswith("__") or not callable(val):
            continue
        setattr(cls, key, trace(val))
        print("Wrapped", key)
    return cls

@mtrace
class dull:
    def method1(self, arg):
        print("Method 1 called with arg", arg)
    def method2(self, arg):
        print("Method 2 called with arg", arg)

@one
def three(x, y):
    print("inside three")
    print("{} and {} like Juicy Fruit gum!".format(x, y))
    print("bye three")


if __name__ == '__main__':
    three('molly', 'milo')
    '''
    d = dull()
    print(d.method1("hello"))
    print(d.method2("there"))
    print(d.__dict__.keys())
    '''

        

