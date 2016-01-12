#!/usr/bin/env python3

a, b, c = "Module a", "Module b", "Module c"

def outer():
    def inner():
        nonlocal b
        global c
        a = "Inner a"
        b = "Inner b"
        c = "Inner c"
        print("inner", a, b, c)
    a = "Outer a"
    b = "Outer b"
    c = "Outer c"
    print("outer", a, b, c)
    inner()
    print("outer", a, b, c)


print("module", a, b, c)
outer()
print("module", a, b, c)

