#!/usr/bin/env python3

'''
extend.py:   demonstrate how to extend a superclass method
'''

class Car:
    def __init__(self, color, cc):
        self.color = color
        self.cc = cc


class Toyota(Car):
    def __init__(self, color, cc, model):
        Car.__init__(self, color, cc)
        self.model = model


class Ford(Car):
    def __init__(self, color, cc, model):
        super().__init__(color, cc)
        self.model = model
