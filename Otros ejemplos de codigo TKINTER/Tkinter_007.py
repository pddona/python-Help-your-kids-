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
#Mouse events	
window.attributes('-topmost',1)
def burp(event):
	mouth_open()
	c.itemconfig(words,text='Burp!')
c.bind_all('<Button-1>',burp) #boton izquierdo
def unburp(event):
	mouth_close()
	c.itemconfig(words,text=' ')
c.bind_all('<Button-3>',unburp) #boton derecho



#Key events
def blink2(event):
	c.itemconfig(eye,fill='green')
	c.itemconfig(eyeball,state=HIDDEN)
def unblink2(event):
	c.itemconfig(eye,fill='white')
	c.itemconfig(eyeball,state=NORMAL)
c.bind_all('<KeyPress-a>',blink2)
c.bind_all('<KeyPress-z>',unblink2)
#Moving with Keys
def eye_control(event):
	key=event.keysym #devuelve tecla pulsada
	if key == "Up":
		c.move(eyeball,0,-1)
	elif key == "Down":
		c.move(eyeball,0,1)
	elif key == "Left":
		c.move(eyeball,-1,0)
	elif key == "Right":
		c.move(eyeball,1,0)
c.bind_all('<Key>',eye_control)



window.mainloop()
