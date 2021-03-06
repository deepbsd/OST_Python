#!/usr/bin/env python3


"""
Creates two entry fields, a button and a label.  When the button is clicked,
the value of each Entry should (if possible) be converted into a float.  If
both conversions succeed, the label should change to the sum of the two
numbers.  Otherwise it should read "***ERROR***"
"""
from tkinter import *

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.text_in = Entry(top_frame)
        self.label = Label(top_frame, text="Number")
        self.text_in.pack()
        self.label.pack()
        top_frame.pack(side=LEFT)

        top_frame = Frame(self)
        self.text_in = Entry(top_frame)
        self.labela = Label(top_frame, text="Number")
        self.text_in.pack()
        self.labela.pack()
        top_frame.pack(side=RIGHT)
        
        

        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM)
        self.labelb = Label(bottom_frame, text="***ERROR***", command=self.multiply)
        self.labelb.pack(side=BOTTOM)
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit)
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Convert", command=self.multiply)
        self.handleb.pack(side=LEFT)

    def multiply(self):
        """Handle a click of the button by processing any text the user has
        placed in the Entry widget according to the selected radio button.
        """
        text = self.text_in.get()
        operation = self.r.get()
        if operation == 1:
            output = text.upper()
        elif operation == 2:
            output = text.lower()
        elif operation == 3:
            output = text.title()
        else:
            output = "***ERROR***"
        self.label.config(text=output)


root = Tk()
app = Application(master=root)
app.mainloop()


