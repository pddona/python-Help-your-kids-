#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from random import *
from time import *
size_x=800
size_y=600
window=Tk()
canvas=Canvas(window,width=size_x,height=size_y)
canvas.pack()
while True:
	col=choice(['pink','red','purple','yellow','orange'])
	x0=randint(0,size_x)
	y0=randint(0,size_y)
	d=randint(0,size_y/5)
	canvas.create_oval(x0,y0,x0+d,y0+d,fill=col)
	window.update()
	sleep(0.5)
window.mainloop()
