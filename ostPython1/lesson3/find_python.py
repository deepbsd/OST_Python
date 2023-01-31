#!/usr/bin/env python3

""" Detect any mention of Python in the user's input  """

user_input = input("Please enter a sentence: ")

if "python" in user_input.lower():
    print("You mentioned python!")
elif "ruby" in user_input.lower():
    print("You mentioned Ruby.")
elif "perl" in user_input.lower():
    print("You mentioned Perl.")
elif "bash" in user_input.lower():
    print("You mentioned Bash.")
else:
    print("Didn't see 'Python' here...")


