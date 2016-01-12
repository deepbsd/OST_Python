#!/usr/bin/env python3

from tkinter import *


ALL = E+W+N+S

"""
class Application(Frame):

    def __init__(self, root):
        #self.frame = Frame(root, width=500, height=500)
        

        firstFrame = Frame(root)
        #firstLabel = Label(firstFrame, text="Frame 1", bg="red", fg="white")
        #firstLabel.grid()
        firstFrame.grid()

        secondFrame = Frame(self.frame)
        secondLabel = Label(secondFrame, text="Frame 2", bg="yellow", fg="black")
        secondLabel.grid(row=1, column=0, sticky=ALL)
        secondFrame.grid(row=1, column=0, rowspan=1, columnspan=1)


        thirdFrame = Frame(self.frame)
        thirdLabel = Label(thirdFrame, text="Frame 3", bg="blue", fg="white")
        thirdLabel.grid(row=0, column=1, sticky=ALL)
        thirdFrame.grid(row=0, column=1, rowspan=2, columnspan=1.5)
"""




root = Tk()
root.title("Hi Pat!")


myLabelA = Label(root, text="Name: ")
myLabelB = Label(root, text="Password: ")
entry_n = Entry(root)
entry_p = Entry(root)

myLabelA.grid(row=0, sticky=E)
myLabelB.grid(row=1, sticky=E)

entry_n.grid(row=0, column=1)
entry_p.grid(row=1, column=1)

cb = Checkbutton(root, text="Keep me logged in?")
cb.grid(columnspan=2)


root.mainloop()
