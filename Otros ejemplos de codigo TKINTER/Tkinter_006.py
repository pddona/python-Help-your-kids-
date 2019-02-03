#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from time import *
window=Tk()
window.title('Alien')

c=Canvas(window,width=400,height=300)
c.pack()
body=c.create_oval(100,150,300,250,fill='green')#coordenadas esquinas superior izquierda e inferior derecha
eye=c.create_oval(170,70,230,130,fill='white')
eyeball=c.create_oval(190,90,210,110,fill='black')
mouth=c.create_oval(150,220,250,240,fill='red')
neck=c.create_line(200,150,200,130)
hat=c.create_polygon(180,75,220,75,200,20,fill='blue')
sleep(1)


def mouth_open():
	c.itemconfig(mouth,fill='black')
def mouth_close():
	c.itemconfig(mouth,fill='red')
def blink():
	c.itemconfig(eye,fill='green')
	c.itemconfig(eyeball,state=HIDDEN)
def unblink():
	c.itemconfig(eye,fill='white')
	c.itemconfig(eyeball,state=NORMAL)
words=c.create_text(200,280,text='I am an Alien')
def steal_hat():
	c.itemconfig(hat,state=HIDDEN)
	c.itemconfig(words,text='Give my hat back')
def thanks():
	c.itemconfig(hat,state=NORMAL)
	c.itemconfig(words,text='Thanks')
while True:	
	#move shapes
	c.move(eyeball,-10,0)
	window.update()
	sleep(0.5)
	
	c.move(eyeball,10,0)
	window.update()
	sleep(0.5)
	
	#changing colors
	
	mouth_open()
	window.update()
	sleep(0.5)
	mouth_close()
	window.update()
	sleep(0.5)
	
	#Hide and show
	
	blink()
	window.update()
	sleep(0.5)
	unblink()
	window.update()
	sleep(0.5)
	
	#Saying things
	
	steal_hat()
	window.update()
	sleep(2)
	thanks()
	window.update()
	sleep(2)

window.mainloop()
