#!/usr/bin/env python3
#
#
#       hello.py
#
#    Lesson 1: Introduction to Eclipse
#
#     by David S. Jackson
#          1/7/2015
#   
#  OST Python2: Getting More Out of Python
#     for Pat Barton, Instructor
#


"""
This is a replacement helloworld.py that no longer 
seems to exist on the Oreilly servers for Python2 Lesson 1
"""



import time

def ImAlive(who):
  "Greets the world"
  now = time.time()
  return "Hello {}! I was born {} seconds after the Epoch!  \nHey, what's an Epoch?".format(who, now)
  

user = input("What is your name? ")

if not user:
  who = 'World'
  print(ImAlive(who))
else:
  who = user
  print(ImAlive(who))


