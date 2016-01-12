#!/usr/bin/env python3
#
#
#         mytree1.py
#
#    Lesson 3: Delegation and Composition
#
#     by David S. Jackson
#          7/15/2015
#          7/16/2015  2nd try...
#   
#  OST Python4: Advanced Python
#     for Pat Barton, Instructor
#

"""
mytree1.py:  assignment for Python4, Lesson3: Delegation and Composition

Modify the logic of the Tree object to:

    *allow data to be stored as an additional attribute of each node (the data
    should be passed as an additional argument to __init__())

    *provide a find() method that locates a key (whose value is passed to
    find() as an argument) and returns the data associated with the node; if
    the key is not present in the tree, the method should raise a KeyError
    exception.


7-16-15 Edit:  1) changed to self.data = value instead of 
                  self.data = {self.key:value}
               2) added __repr__(self):
               3) changed walk output to yield self, which outputs __repr__
               format
               4) changed find() method to look for 'obj' in self.walk() and return obj.data
               5) changed insert() to account for self.data not being a dict.

"""


class Tree:
    def __init__(self, key, value):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        #self.data = {self.key:value}
        self.data = value
        self.left = self.right = None

    def __repr__(self):
        "Make a nice output format..."
        return "{}:{}".format(self.key, self.data)

    def insert(self, key, value):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Tree(key, value)
        elif key > self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Tree(key, value)
        else:
            raise ValueError("Attempt to insert duplicate value")

    def walk(self):
        "Generate the keys _and values_ from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self
        if self.right:
            for n in self.right.walk():
                yield n

    def find(self, key):
        "Find a value for a key that exists in the tree; KeyError otherwise"
        for obj in self.walk():
            if obj.key == key:
                return obj.data

        raise KeyError("{} not in existing data...".format(key))


if __name__ == "__main__":
    t = Tree("D", "delta")
    mydict = {'B':"bravo", 'J':"juliette", 'Q':"quebec", 'K':'kilo',
            'F':'foxtrot', 'A':'alpha', 'C':'charlie'}
    for k,v in mydict.items():
        t.insert(k,v)

    # t.data will only show the last piece of data, now that self.data is not a
    # dict...
    print("t.data: ", t.data)

    # To get all node.key's and node.data's, need to do a list of walk() ...
    print("t.walk: ", list(t.walk()))
    # Test the find() method with a good key
    print("Good key testing t.find('J'): ", t.find('J'))
    # Test for the KeyError on find() with a bad key:
    try:
        print("Bad key testing t.find('W'): ", t.find('W'))
    except KeyError:
        print("Bad key testing t.find('W'):  Yay!  We have a wonderful little KeyError!")
