#!/usr/bin/env python3


# Python1 Lesson 3 
# guesser.py


target = 63
guess = 0

while guess != target:
    guess = int(input("Guess an integer: "))
    if guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")
    else:
        print("Just right!")
