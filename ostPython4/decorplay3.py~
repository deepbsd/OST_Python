#!/usr/bin/env python3


counts = {}
def countable(ftype):
    "Returns a decorator that counts each call of a function against ftype."
    def decorator(f):
        "Deocrates a function and to count each call."
        def wrapper(*args, **kw):
            "Counts every call as being of the given type."
            try:
                counts[ftype] += 1
            except KeyError:
                counts[ftype] = 1
            return f(*args, **kw)
        return wrapper
    return decorator

@countable("f1")
def f1(a, b=None):
    print("f1 called with", a, b)

@countable("f2")
def f2():
    print("f2 called")

@countable("f3")
def f3(*args, **kw):
    print("f3 called:", args, kw)

for i in range(20):
    f1(1)
    f2()
    f3(i, i*i, a=i)


for k in sorted(counts.keys()):
    print(k, ":", counts[k])
