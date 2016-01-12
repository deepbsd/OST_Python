#!/usr/bin/env python3
#
#            floatsum.py
#
#   for OST: Lesson 7: Intro to GUIs
#
#    by David Jackson on Feb 9 2015
#
#        Instructor:  Pat Barton
#
#
"""
This program is a simple GUI with two Entry fields, a button, and a label.
When the button is clicked, the value from each Entry field be converted 
into a float, if possible.  If both conversions succeed, the label should
change to the sum of the two numbers.  Otherwise it reads "***ERROR***"
"""

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):     
        top_frame = Frame(self)
        self.num1_in = Entry(top_frame)
        self.num2_in = Entry(top_frame)
        self.label = Label(top_frame, text="Enter Integers")
        self.num1_in.pack(side=LEFT)
        self.num2_in.pack(side=RIGHT)
        self.label.pack()
        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.handleb = Button(bottom_frame, text="Sum", command=self.num_sum)
        self.handleb.pack(side=LEFT)

    def num_sum(self):
        num1 = self.num1_in.get()
        num2 = self.num2_in.get()
        try:
            num1 = int(num1)
            num2 = int(num2)
            output = num1 + num2
            output = float(output)
        except ValueError:
            output = "***ERROR***"
        self.label.config(text=output)

        
root = Tk()
app = Application(master=root)
app.mainloop()
