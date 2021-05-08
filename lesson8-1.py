# -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:09:34 2021

@author: Admin
"""

import turtle
import time
import datetime
tur = turtle.Turtle()

tur.speed(10)

def writeNumber(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()
    
tur.seth(90)


for i in range(1, 13):
    tur.right(30)
    writeNumber(i)
    

tur.penup()
tur.forward(230)
tur.right(270)
tur.pendown()
tur.circle(230)
tur.hideturtle()

    
update = True
updateSecond = True

while True:
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    if update:
        hour = turtle.Turtle()
        hour.pensize(2)
        hour.color(1,0,0)
        hour.seth(90)
        hour.right((h + m / 60) * 30)
        hour.forward(90)
        
        
        minute = turtle.Turtle()
        minute.pensize(2)
        minute.color(0,0,1)
        minute.seth(90)
        minute.right(m * 6)
        minute.forward(145)
        update = False
        
    if updateSecond:
        second = turtle.Turtle()
        
        second.seth(90)
        second.right(s * 6)
        second.forward(180)
        updateSecond = False
        
    time.sleep(1)
    now = datetime.datetime.now()
    mNew = now.minute
    sNew = now.second
    
    
        
    if mNew != m:
        update = True
        hour.clear()
        hour.reset()
        minute.clear()
        minute.reset()
        
    if sNew != s:
        updateSecond = True 
        second.clear()
        second.reset()
        second.hideturtle()
        

turtle.done()
turtle.exitonClick()