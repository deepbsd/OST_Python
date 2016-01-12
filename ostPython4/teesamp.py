#!/usr/bin/env python3

"""
Demonstrate simple use of itertools.tee
"""

import itertools

actions = "save", "delete"
data = ["file1.py", "file2.py", "save", "file3.py", "file4.py", "delete", "file 5.py", "save", "file6.py", "file7.py", "file8.py", "file9.py", "save"]


saved = []
deleted = []

def datagen(d):
    "a toy data generator using static data"
    for item in d:
        yield item

commands, files = itertools.tee(datagen(data))

# commands and files are <itertools_tee objects!
print(commands, files)


for action in commands:
    if action in actions:
        for file in files:
            if file == action:
                break
            if action == "save":
                saved.append(file)
            elif action == "delete":
                deleted.append(file)

print("Saved:", ", ".join(saved))
print("Deleted:", ", ".join(deleted))


