#!/usr/bin/env python3




def framework(f):
    f.happy = 'Yay!'
    f.sad = 'Argh. Boo hoo.  So sad!'
    return f

@framework
def somefunc(x):
    pass

if __name__ == "__main__":
    print(somefunc.happy)
    print(somefunc.sad)
