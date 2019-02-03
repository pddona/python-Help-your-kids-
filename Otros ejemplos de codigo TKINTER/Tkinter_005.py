#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
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
window.mainloop()
