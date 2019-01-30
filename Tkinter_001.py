#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
def bAaction():
	print('Thank you')
def bBaction():
	print('Upsss')
window=Tk()
buttonA=Button(window,text='Press me',command=bAaction)
buttonB=Button(window,text='Dont Press me',command=bBaction)
buttonA.pack()
buttonB.pack()
window.mainloop()
