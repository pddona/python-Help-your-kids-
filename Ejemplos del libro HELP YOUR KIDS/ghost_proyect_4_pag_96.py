#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1,3)
    print('Tenemos tres puertas')
    print('hay un fantasma detrás de una de ellas')
    print('¿Qué puerta eliges?')
    door = input('¿ 1,2 o 3 ?')
    door_num = int(door)
    if door_num == ghost_door:
        print('Ghost!!!!')
        feeling_brave = False
    else:
        print('No hay fantasma')
        print('has entrado en otra habitación')
        score = score +1
print('Corre!!!!')
salida = 'Game Over  Tu Puntuación es:' + str(score) 
print(salida)
#print('Game Over    Tu Puntuación es:' , score)
