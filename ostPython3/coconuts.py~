#!/usr/bin/env python3
#
#
#          coconuts.py
#
#    Lesson 2: Converting Data to 
#       Structured Objects
#
#     by David S. Jackson
#          4/23/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#
"""
coconuts.py contains an inventory class that tracks different types of coconuts
from around the world.  The different types of coconuts must have these weight
attribute values (South Asian: 3; Middle Eastern: 2.5; American: 3.5)  The
inventory class must have the following methods: add_coconut(), which accepts
a coconut as an argument.  Other types throw an AttributeError.  And
total_weight(), which provides the total weight of coconuts.  
I have also used the isinstance built-in as recommended.
The test program must check:
1. that different coconut types each have a different weight.
2. that if a string object is passed to Inventory.add_coconut method, an
   AttributeError is thrown
3. that if 2 South Asian, 1 Middle Eastern, and 3 American coconuts are added
   to the inventory, the Inventory.total_weight() method returns 19.
"""

class Coconut:
    "Just a container for the respective kinds of coconuts."
    pass

class SouthAsian(Coconut):
    "South Asian style coconuts"
    weight = 3

class MiddleEastern(Coconut):
    "Middle Eastern style coconuts, the lightest style"
    weight = 2.5

class American(Coconut):
    "American, my favorite and heaviest coconut!"
    weight = 3.5


class Inventory(object):
    """
    Initializes the "basket" of coconuts.  Also includes the add_coconut() 
    and total_weight() methods.  Everything you need to keep your lovely
    basket of coconuts happy and health!
    """


    def __init__(self):
        """
        Initializes the inventory and creates the 'basket' for the nuts to go
        in.
        """
        self.nuts = []


    def add_coconut(self, obj):
        "Add coconut type to inventory of with quantity num"
        if isinstance(obj, Coconut):
            self.nuts.append(obj)
        else:
            raise AttributeError("Coconut type is not recognized by Inventory class!")



    def total_weight(self):
        "Returns the total weight of all coconuts in inventory"
        total = 0
        #for value in self.nuts: total += value.weight
        total = sum([value.weight for value in self.nuts])
        return total



if __name__ == "__main__":

    a = SouthAsian()
    b = MiddleEastern()
    c = American()
    basket = Inventory()
    for n in range(2): basket.add_coconut(a)
    for n in range(1): basket.add_coconut(b)
    for n in range(3): basket.add_coconut(c)
    print(basket.total_weight())
