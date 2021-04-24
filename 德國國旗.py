# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:03:10 2021

@author: Admin
"""

import turtle
tur = turtle.Turtle()

def rectangle():
    tur.begin_fill()
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.end_fill()
    
    
def myGoto(x, y):
    tur.penup()
    tur.goto(x, y)
    turtle.pendown()   
    
turtle.setup(850,650, 0, 0)
tur.penup()
tur.goto(-400, 300)
tur.pendown()
tur.fillcolor(0,0,0)
tur.begin_fill()
rectangle()
tur.end_fill()

tur.penup()
tur.goto(-400, 100)
tur.pendown()
tur.fillcolor(1,0,0)
tur.begin_fill()
rectangle()
tur.end_fill()

tur.penup()
tur.goto(-400, -100)
tur.pendown()
tur.fillcolor(1,1,0)
tur.begin_fill()
rectangle()
tur.end_fill()
tur.right(90)
tur.forward(200)
tur.right(270)


    
    




turtle.done()
turtle.exitonclick()

