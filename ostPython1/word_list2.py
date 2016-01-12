#!/usr/local/bin/python3

# Get a string from user with upper case and lower case words
# Create a list of words with only lower case letters and another list with
# upper case letters.  Two lists.  Print out each list and the words in them.

da_string = input("Please input your text: ")

lc_list = []
UC_list = []

for word in da_string.split(" "):
    if word.islower():
        lc_list.append(word)
    else:
        UC_list.append(word)



for word in UC_list + lc_list :
    print(word)
