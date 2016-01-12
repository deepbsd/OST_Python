#!/usr/bin/env python3
#
#
#       furnishings.py
#
#    Lesson 7: Python's Object 
#       Oriented Features
#
#     by David S. Jackson
#          5/3/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#

"""
This program tests the student's ability to create classes that
inherit desired functionality from parent classes and to uses 
them resourcefully in practice.  furnishings.py creates a parent
class called Furnishings with a required 'room' attribute.  Child
classes--namely, Bed, Bookshelf, Sofa, and Table--must inherit 
this required attribute when they are being instantiated in the 
program.  The map_the_home() function/method takes the list of
Furnishing objects and creates a 'homedict' object with the room
as key for each furnishings object.  That is, the dictionary will
contain values like:  
{'Bedroom': [<furnishings.Bed object at 0x39f3b0>], } and so on.
Only the map_the_home() function requires testing.  The counter()
function, however, goes a little beyond the assigned requirement.  
It returns a 'furndict' dictionary with counts for each room in
the home.  The rooms in the house are keys for this dictionary,
and the counts for each piece of furniture in the home are the
values in the dictionary.
"""

class Furnishings(object):
    def __init__(self, room):
        self.room = room

class Sofa(Furnishings):
    pass

class Bookshelf(Furnishings):
    pass

class Bed(Furnishings):
    pass

class Table(Furnishings):
    pass

def map_the_home(home):
    """
    'home' must be a list of Furnishings objects; method returns a 
    dictionary of furnishings objects where each room is a key and 
    each value is a list of furnishings objects in that room.
    """
    homedict = {}
    roomlist = set(home[n].room for n, v in enumerate(home))
    for rm in roomlist:
        rmlst = []
        for n, v in enumerate(home):
            if home[n].room == rm:
                rmlst.append(v)
        homedict[rm] = rmlst
    return homedict



def counter(home):
    """
    Counts Furnishings objects by type and room and returns a dictionary
    of these values.  If called by module other than
    the main module, this function *won't* print out
    a list of values.  Otherwise, it will.
    Furndict sample format:  Bookshelves: 2, Sofas: 1 and so on...
    """
    furniture = ('Beds', 'Bookshelves', 'Sofas', 'Tables')
    beds=0; bookshelves=0; sofas=0; tables=0
    for v in home:
        if isinstance(v, Bed):
            beds += 1
        if isinstance(v, Bookshelf):
            bookshelves += 1
        if isinstance(v, Sofa):
            sofas += 1
        if isinstance(v, Table):
            tables += 1
    counts = (beds, bookshelves, sofas, tables)
    furndict = dict(zip(furniture, counts))
    if __name__ == "__main__":
        for k, v in furndict.items():
            print("{}: {}".format(k, v))
    return furndict



if __name__ == "__main__":

    home = []
    home.append(Bed('Bedroom'))
    home.append(Table('Bedroom'))
    home.append(Bookshelf('Basement'))
    home.append(Sofa('Basement'))
    home.append(Sofa('Living Room'))
    home.append(Table('Dining Room'))

    print()
    print(map_the_home(home))
    print()
    counter(home)


