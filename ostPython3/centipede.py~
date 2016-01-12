#!/usr/bin/env python3
#
#
#       centipede.py
#
#    Lesson 9: Advanced Objects:
#        Special Methods
#
#     by David S. Jackson
#          5/15/2015
#   
#  OST Python3: The Python Environment
#     for Kirby Urner, Instructor
#

'''
Created a class called Centipede that has two attributes: stomach and legs,
which are internal lists.  The first is a list of arguments the instance gets
called with, which are typically food.  Ie, ralph = Centipede()  and   
ralph('food type').  'food type' would get added to an internal stomach list.
Attributes that are set for the instance, such as ralph.happy = 'yes', get
added to another internal list called 'legs'.  One of the challenges of this
assignment is to add those lists in such a way that they do not trigger
__setattr__ when they are called, or else 'stomach' and 'legs' themselves get
added to the internal attributes list, called 'legs'.

Further, __str__ and __repr__ must be set, so that __str__ returns a comma
separated list of stomach contents (no spaces), and __repr__ returns a 
comma separated list of internal attributes that have been reassigned, such
as ralph.happy = 'yes' mentioned above.  

The internal attributes of self.legs and self.stomach must further be protected
so that if someone tries to use __setattr__ to override the instance values for
those attributes, an AttributeError gets raised with the warning: "For internal
use only."

The file test_centipede.py is provided as part of the assignment.
'''


class Centipede():

    def __init__(self):
        """
        Initializes a centipede type object for instances of Centipede.
        This format of initializing the internal stomach and legs lists
        avoids triggering __setattr__ whenever an instance is 
        initialized.

        This method of initializing the self.stomach and self.legs lists
        uses __getitem__ to bypass __setattr__ .
        """
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []

    def __str__(self):
        "Makes a nice comma separated list of items in self.stomach"
        return ','.join(self.stomach)

    def __repr__(self):
        "Makes a nice comma separated list of attributes for self.legs"
        return ','.join(self.legs)

    def __call__(self, arg):
        """
        Helps Centipede be 'callable' and appends all arguments used
        in calling the instance to be contained in the stomach list.
        """
        self.stomach.append(arg)

    def __setattr__(self, key, value):
        """
        The internal lists self.stomach and self.legs are protected
        from being overridden by a user of a Centipede instance.  Also,
        this method Adds key:value to __dict__ and also key to self.legs.
        """
        if key == 'stomach' or key == 'legs':
            raise AttributeError("{0} is for internal use only".format(key))
        self.__dict__[key] = value
        self.legs.append(key)


if __name__ == "__main__":

    ralph = Centipede()
    ralph('pretzel')
    ralph('yogurt')
    ralph('wild turkey')
    ralph.car = 'chevy'
    ralph.boat = 'sail'
    print(ralph)
    print(ralph.legs)
    print(repr(ralph))
    try:
        ralph.legs = 'lots'
    except AttributeError:
        print("Yay!  We did it right!")



