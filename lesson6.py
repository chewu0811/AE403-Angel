# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:07:45 2021

@author: Admin
"""

import turtle
tur = turtle.Turtle()


def square():
    for i in range(4):
        tur.forward(100)
        tur.right(90)
        
tur.fillcolor(1,0,0)

turtle.setup(500, 500)
tur.penup()
tur.goto(-100, 100)
tur.pendown()
tur.fillcolor(1,0,0)
tur.begin_fill()
square()
tur.end_fill()

tur.penup()
tur.goto(0, 0)
tur.pendown()
tur.fillcolor(0,1,0)
tur.begin_fill()
square()
tur.end_fill()

turtle.done()
turtle.exitonclick()


