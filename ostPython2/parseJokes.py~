#!/usr/bin/env python3

"""
The purpose of this code is to parse the 'jokes.txt' file
for Lesson 13 (emailJoker.py).  This code could then be
added to the emailJoker.py module to create actual jokes
instead of stub jokes as they have now...
"""

filehandle = open('jokes.txt', 'r')
filetext = filehandle.readlines()
filehandle.close()

joke = ''
jokeDB = []

for line in filetext:
    if line != '%\n':
        joke += line
    else:
        jokeDB.append(joke)
        joke = ''


for num, value in enumerate(set(jokes)):
    print("Joke %s: \n%s\n" % (num, value))

#length = len(set(jokes))

#print(length, " jokes")
