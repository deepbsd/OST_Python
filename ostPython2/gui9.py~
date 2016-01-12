#!/usr/bin/env python3
#
#         gui9.py
#
#      for OST Lesson 9
#         2/28/15
#           by
#     David S. Jackson
#          for
#  Instructor Pat Barton
#
"""
Starting with the project you created at the end of the last lesson, add
components to the existing framework so that:
oWhen an area occupied by Frame 1 or Frame 2 is clicked with mouse button 1,
the program should print which frame was clicked and the X and Y coordinates
(relative to the Frame).
oFrame 3 should contain an Entry and a Text widget. When the button now
labeled "Open" is clicked, the content of the Entry should be used as a file
name, and the content of the file (if any) displayed in the Text widget.
oThe Entry and Text widgets should completely fill Frame 3 and continue to do
so even as the application window is resized.
oThe color of the text displayed in Frame 3's Text widget should change
appropriately when the "Red," "Blue," "Green," or "Black" buttons are clicked.
"""

from tkinter import *

ALL = N+S+E+W


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        self.createWidgits()

    def handler1(self, event):
        print("Frame 1 clicked at", event.x, event.y)

    def handler2(self, event):
        print("Frame 2 clicked at", event.x, event.y)

    def colorChange(self, color):
        print("Changing text color to {0}".format(color))
        self.textbox.config(foreground=color)
        self.textbox.update()


    def setText(self, filename):
        try:
            filename = self.entry.get()
            intext = open(filename, 'r').read()
            self.text = intext
            self.textbox.delete('1.0', END)
            self.textbox.insert(END, self.text)
            self.textbox.grid()
        except Exception:
            print("Can't find file to open...")


    def createWidgits(self):
        # frame and label creation
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        for i in range(5):  self.columnconfigure(i, weight=1)

        frame1 = Frame(self, bg='red', name='frame 1')
        frame2 = Frame(self, bg='blue', name='frame 2')
        frame3 = Frame(self, bg='green', name='frame 3')

        frame1.bind("<Button-1>", self.handler1)
        frame2.bind("<Button-1>", self.handler2)

        label1 = Label(frame1, bg='red', text="Frame 1").grid()
        label2 = Label(frame2, bg='blue', text="Frame 2").grid()

        frame1.grid(sticky=ALL, row=0, column=0, columnspan=2)
        frame2.grid(sticky=ALL, row=1, column=0, columnspan=2)
        frame3.grid(sticky=ALL, row=0, column=2, columnspan=3, rowspan=2)

        # frame 3 objects
        self.entry = Entry(frame3, borderwidth=2)
        self.entry.grid(sticky=E+W, row=0)
        self.textbox = Text(frame3)
        self.textbox.grid(sticky=ALL, row=1)

        filename = self.entry.get()

        # I guess I don't need the return key active here...
        #self.entry.bind('<Return>', (lambda event: setText(filename)))

        # Make the buttons...
        b_options = ['Red', 'Blue', 'Green', 'Black', 'Open']
        for i, op in enumerate(b_options):
            if op == 'Open':
                doit = lambda: self.setText(filename)
            elif op == 'Red':
                doit = lambda: self.colorChange("red")
            elif op == 'Blue':
                doit = lambda: self.colorChange("blue")
            elif op == 'Green':
                doit = lambda: self.colorChange("green")
            elif op == 'Black':
                doit = lambda: self.colorChange("black")
            else:
                print("How the hell did we get here???")

            b = Button(self, text=op, width=100, command=doit)
            b.grid(row=2, column=i, columnspan=1, rowspan=1, sticky=E+W)

        # configures
        frame3.columnconfigure(0, weight=1)
        frame3.rowconfigure(0, weight=1)
        frame3.rowconfigure(1, weight=1)


root = Tk()
root.geometry('700x400')
app = Application(master=root)
app.mainloop()



