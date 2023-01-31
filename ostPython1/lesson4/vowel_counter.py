#!/usr/bin/env python3

"""Counts the vowels in a user input string"""


s = input("Enter any string: ")
vcount = 0

for c in s:
    if c in "aeiouAIEOU": 
        vcount += 1
    print("C is ",c, "; Vowel count:",vcount )
