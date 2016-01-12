#!/usr/bin/env python3


class MyClass:

    @staticmethod
    def f(name):
        return name.upper()


if __name__ == "__main__":
    d = MyClass()
    #print("d() says:", d.f('hi'))
    print(d.f('hi'))

