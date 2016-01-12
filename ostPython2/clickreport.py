#!/usr/bin/env python3

from tkinter import *

root = Tk()

def handler(event):
    print("clicked at", event.x, event.y)

frame = Frame(root, width=400, height=300)
frame.bind("<Button-1>", handler)
frame.pack()

root.mainloop()
