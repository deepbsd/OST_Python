#!/usr/bin/env python3
#
#
#             tkpframes.py
#         (Uses "pack" manager)
#
#      for OST Lesson 8: GUILayout
#
#      by David S Jackson on 2/18/15
#
#          Instructor:  Pat Barton
#
"""
Write a GUI-based program to build a window layout as shown
below (not copied into this program).  When the frame is
resized, the buttons should stay the same height and expand
sideways.  Frame 1 and 2 should always be the same height
and width as each other, and Frame 3 should be half as wide
again as they are (ie, 150% wider, as shown below).  
Labeling each Frame is optional/good exercise.

"""
from tkinter import *

root = Tk()
root.title("Hi Pat!")

# Use 2 Horizontal Frames
frame1 = Frame(root)
frame2 = Frame(root)

# Use 3 Labels, 2 in the first frame, 1 in the second
# Frame 3 is 50% wider than Frames 1 and 2
# Frame 3 height is equal to height of 1 and 2 together
label_1 = Label(frame1, text="Frame 1")
label_1.config(bg="green", height=10, width=10)
label_2 = Label(frame1, text="Frame 2")
label_2.config(bg="yellow", height=10, width=10)
label_3 = Label(frame2, text="Frame 3")
label_3.config(bg="blue", height=20, width=15)

# Add 2 buttons to Frame 1, 3 buttons to Frame 2
button_1 = Button(frame1, text="Button 1")
button_2 = Button(frame1, text="Button 2")
button_3 = Button(frame2, text="Button 3")
button_4 = Button(frame2, text="Button 4")
button_5 = Button(frame2, text="Button 5")

# Labels all should resize in both X & Y axis
label_1.pack(side=TOP, expand=YES, fill=BOTH)
label_2.pack(side=TOP, expand=YES, fill=BOTH)
label_3.pack(side=TOP, expand=YES, fill=BOTH)

# Buttons should expand only in X axis
button_1.pack(side=LEFT, expand=YES, fill=X)
button_2.pack(side=LEFT, expand=YES, fill=X)
button_3.pack(side=LEFT, expand=YES, fill=X)
button_4.pack(side=LEFT, expand=YES, fill=X)
button_5.pack(side=LEFT, expand=YES, fill=X)

# Frames 1 and 2 should be anchored together and 
# fill together when resized
frame1.pack(side=LEFT, expand=YES, fill=BOTH, anchor=SE)
frame2.pack(side=LEFT, expand=YES, fill=BOTH, anchor=SE)



root.mainloop()
