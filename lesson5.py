# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:04:52 2021

@author: Admin
"""

x = 220
print(id(x))

x = 254
print(id(x))

y = 254
print(id(y))


def myfunction():
    print("test")
    
myfunction()          
print(id(myfunction))
print(hex(id( myfunction)))

a =  myfunction
a()
