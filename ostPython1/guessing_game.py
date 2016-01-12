#!/usr/bin/env python3
#
#
#      guessing_game.py
#
#    Lesson 12: The Python 
#       Standard Library
#
#     by David S. Jackson
#          12/6/2014
#   
#  OST Python1: Beginning Python
#     for Pat Barton, Instructor
#
'''
Lab 12: Objective 1   Guessing game that imports random module
Objective:

This project tests your ability to use modules and imports.

    1. Create a new Python source file named guessing_game.py.
    2. Import the random module.
    3. Use the help() function on the random module to determine how to generate a random number between 1 and 99 inclusive.
    4. Generate a random number between 1 and 99 and store it in a variable.
    5. Use a while loop to accept integers from the user (don't forget?you'll need to convert the input string).
    6. Compare the user's guess with the saved random number.
    7. If the user successfully guesses the target number, inform them and terminate the program.
    8. Otherwise, inform the user whether their guess was higher or lower than the saved random number and loop around to allow them to guess again.

Below is an example of possible output from running the program.

Guess a number: 25
Too low
Guess a number: 75
Too high
Guess a number: 60
Too high
Guess a number: 45
Too low
Guess a number: 53
You guessed it!


'''
import random

pc_choice = random.randint(1,99)
guesses = []
print("\nWelcome to the Number Guessing Game!\nThe Computer has picked a number between 1 and 99.\nEnter a number or press <ENTER> to stop playing.\n")

# Note:  today is 8/8/15, and I'm going back through this code for archival
# purposes.  I didn't know about try(): at this point in time.  Before I set
# user_guess = int(user_guess) I would have put that inside a try() statement.
# But this code is how I did it then...

while True:
    user_guess = input("What is your guess? ")
    #if user_guess == "" :   # fixed per Pat's comments Aug/8/15
    if not user_guess:
        print("Bye! Thanks for playing!")
        break
    user_guess = int(user_guess)
    if user_guess in guesses :
        print("you already guessed this number!")
    elif user_guess not in guesses :
        guesses.append(user_guess)
    if user_guess > 99 or user_guess < 0 :
        print("Pick a number between 1 and 99 only! ")
        continue
    if user_guess > pc_choice :
        print("Your guess is too high...")
    elif user_guess < pc_choice :
        print("Your guess is too low...")
    elif user_guess == pc_choice :
        print("Great guess! ",pc_choice," is right!  You win!")
        break
