#!/usr/local/bin/python3
#
#
#            guess.py
#
#    Lesson 4: Iteration: 
#       For and While Loops
#
#     by David S. Jackson
#          11/26/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
"""
I notice this program works fine with python 2.7 but not with 3.4.  In
particular the (5-tries) part gets an error about types that can't work
together: "None" and "int"
"""

secret = 17
tries = 0


while tries <= 4 :    # 0 thru 4 is five counts...
    guess = input("I'm thinking of a number between 1 and 20.  Your guess: ")
    guess = int(guess)
    if guess < secret :
        print("Guess higher... ")
        tries += 1
        print(5-tries, " tries remaining...")
    elif guess > secret :
        print("Guess lower... ")
        tries += 1
        print(5-tries, " tries remaining...")
    elif guess == secret :
        tries += 1
        print("Awesome Job!  You win a European Swallow! (Or was it African?)")
        print("You guessed it in", tries, "tries!") 
        break
        

