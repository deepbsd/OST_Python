#!/usr/bin/env python3
#
#
#       doggies.py
#
#    Lesson 14: Classes and 
#    Object-Oriented Programming
#
#     by David S. Jackson
#          12/9/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
""" 
Project tests more understanding of classes and objects 
This project tests more of your understanding of classes and objects.

    1. Create a new Python source file named doggies.py.
    2. Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the implicit self.
    3. Bind an empty list to a dogs global variable (dogs should not be an attribute of the Dog class).
    4. Using a while loop, get user input for name and breed. The loop should terminate when the user enters a blank name.
    5. For each name and breed entered, create an instance of the Dog class with name and breed as arguments. Append the object to the dogs list.
    6. Each time around the loop, print the current dogs list (the name and breed of each dog).

Below is an example of possible output from running the program.

Name: Snoopy
Breed: Beagle
DOGS
0. Snoopy:Beagle
****************************************
Name: Marmaduke
Breed: Great Dane
DOGS
0. Snoopy:Beagle
1. Marmaduke:Great Dane
****************************************
Name: Rover
Breed: Mutt
DOGS
0. Snoopy:Beagle
1. Marmaduke:Great Dane
2. Rover:Mutt
****************************************
Name:


"""

class Dog:
    """ Consists of name and breed """
    def __init__(self, name, breed):
        """ initialize class """
        self.name = name
        self.breed = breed

    def __str___(self, name, breed):
        """ call when printing out strings of Dog """
        return "%s:%s" % (self.name, self.breed)


dogs = []

if __name__ == "__main__":

    while True:
        name = input("Please enter dog's name: ")
        if not name:
            print("Leaving now.  Good bye!")
            break
        breed = input("Please enter dog's breed: ")

        thing = Dog(name, breed)
        dogs.append(thing)

        print("======== Our Dogs ========")
        for i, thing in enumerate(dogs, start=1):
            print("{0}. {1}: {2}".format(i, thing.name, thing.breed))
        print("*" * 40)
        



