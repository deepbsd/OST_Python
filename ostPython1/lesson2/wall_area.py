#!/usr/bin/env python3

#
# wall_area.py
#

intro_string = "This program calculates the area of the walls of a room after accepting the height, width, and depth of the room."

print(intro_string)

h = float(input("Room height: "))
w = float(input("Room width: "))
d = float(input("Room depth: "))

area = 2 * (h * (w + d))
print("Area of walls: ", area)
