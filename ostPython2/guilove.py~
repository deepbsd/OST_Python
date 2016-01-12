#!/usr/bin/env python3


from tkinter import *


ALL=N+S+E+W
wt = 1

class App1(Frame):

    def __init__(self, master=None):
        # Overall container
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        self.CreateWidgets()

    def CreateWidgets(self, master=None):
        # slave containers...
        frame1 = Frame(self)
        frame2 = Frame(self)
        frame3 = Frame(self)

        # Use grid() to set up frames1 and 2...
        # Two rows, one column
        for r in (0, 1):
            frame1.rowconfigure(r, weight=1)
            frame2.rowconfigure(r, weight=1)
                
        frame1.columnconfigure(0, weight=1)
        frame2.columnconfigure(0, weight=1)

        
        # Place frame 1 and frame 2
        frame1.grid(row=0, column=0, sticky=ALL)
        frame2.grid(row=1, column=0, sticky=ALL)


        # Label 1
        label_1 = Label(frame1, text="Frame 1")
        label_1.config(bg="green", height=10, width=10)
        label_1.bind("<Button-1>", self.handler1)
        label_1.grid(row=0, column=0, sticky=ALL)

        # Label 2
        label_2 = Label(frame2, text="Frame 2")
        label_2.config(bg="yellow", height=10, width=10)
        label_2.bind("<Button-1>", self.handler2)
        label_2.grid(row=1, column=0, sticky=ALL)

        # Finally, frame 3
        frame3.rowconfigure(0, weight=1)
        frame3.rowconfigure(1, weight=1)
        frame3.columnconfigure(1, weight=1)
        frame3.grid(row=0, column=1, rowspan=2, columnspan=1, sticky=ALL)
        frame3.focus()

        # Entry box using pack()
        my_entry = Entry(frame3)
        my_entry.pack(side=TOP, expand=YES, fill=X, anchor=NE)

        # Text Box using pack()
        my_text = Text(frame3)
        my_text.pack(side=TOP, expand=YES, fill=BOTH, anchor=NE)



    def handler1(self, event):
        print("Frame 1: Clicked at", event.x, event.y)

    def handler2(self, event):
        print("Frame 2: Clicked at", event.x, event.y)





if __name__ == '__main__':

    root = Tk()
    app = App1(master=root)
    app.mainloop()




