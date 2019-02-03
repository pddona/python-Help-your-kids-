#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
window=Tk()
drawing=Canvas(window,width=500,height=500)
drawing.pack()
rect=drawing.create_rectangle(100,100,300,200)
square1=drawing.create_rectangle(30,30,80,80)
oval1=drawing.create_oval(100,100,300,200)
circle1=drawing.create_oval(30,30,80,80)
window.mainloop()
