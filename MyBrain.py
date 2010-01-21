#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from Tkinter import *
import sys,random,time
from openbrain import *

class App:
    def __init__(self, master):
        frame = Frame(master, width=800, height=600)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.procListbox = Listbox(frame, selectmode=EXTENDED)
        self.procListbox.bind("<Double-Button-1>", self.procListboxSelect)
        self.procListbox.pack(side=RIGHT)

        self.exptListbox = Listbox(frame, selectmode=EXTENDED)
        self.exptListbox.bind("<Double-Button-1>", self.exptListboxSelect)
        self.exptListbox.pack()

        self.DoIt = Button(frame, text="Do It Now!", fg="blue", command=self.DoItNow)
        self.DoIt.pack(side=RIGHT)
        self.openBrainInit()

    def openBrainInit(self):
        self.Brain = OpenBrain()
        for expt in self.Brain.Experiments:
            self.exptListbox.insert(END, expt.name)

        for p in ['PSTH', 'Psych', 'AutoCorrelogram']:
            self.procListbox.insert(END, p)
 
        
    def say_hi(self):
        print "hi there, everyone!"

    def exptListboxSelect(self, arrgg):
        print dir(arrgg)

    def procListboxSelect(self, arrgg):
        print dir(arrgg)

    def DoItNow(self):
        print "Do it NOW?"


if __name__ == "__main__":

    #make a main window
    root = Tk()
    app = App(root) 

    #main loop for the main window
    root.mainloop()
    sys.exit()
 
