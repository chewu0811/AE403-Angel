# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:06:09 2021

@author: Admin
"""

import turtle
tur = turtle.Turtle()

def writeNumber(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()
    
tur.seth(60)

for i in range(1, 13):
    writeNumber(i)
    tur.fight(30)
    
    



turtle.done()
turtle.exitonClick()
