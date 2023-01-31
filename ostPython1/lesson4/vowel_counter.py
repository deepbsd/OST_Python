#!/usr/bin/env python3

"""Counts the vowels in a user input string"""


s = input("Enter any string: ")
vcount = 0

for c in s:
    if c in "aeiouAIEOU": 
        vcount += 1
    #print("C is ",c, "; Vowel count:",vcount )

# Assume we no longer want to see the incrementing of the vowel count,
# just show us the final count of the vowels
print("You have ",vcount, " vowels!")
