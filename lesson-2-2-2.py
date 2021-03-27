# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 08:37:26 2021

@author: Admin
"""

import tkinter as tk

window = tk.Tk()

window.title("Menu")

window.geometry("500x500")


string = tk.StringVar()
gender = tk.StringVar()
string.set("Minecraft Python")
gender.set("boy")
def selection():
    label.config(text = "I like " + string.get() + "I am a " + gender.get())
    
    
    
label=  tk.Label(window, bg='#f00', text='尚未選擇')
label.pack()

radio1 = tk.Radiobutton(window,
            text='Minecraft Python',
            variable=string, value='Minecraft Python',
            command=selection)

radio1.pack()

radio2 = tk.Radiobutton(window,
            text='Pygame',
            variable=string, value='Pygame',
            command=selection)

radio2.pack()


radio3 = tk.Radiobutton(window,
            text='tkinter',
            variable=string, value='tkinter',
            command=selection)

radio3.pack()

radio4 = tk.Radiobutton(window,
            text='boy',
            variable=gender, value='boy',
            command=selection)

radio4.pack()

radio5 = tk.Radiobutton(window,
            text='girl',
            variable=gender, value='girl',
            command=selection)

menuBar = tk.Menu(window)

fileMenu = tk.Menu(menuBar,tearoff=False)

fileMenu.add_command(label="new game")

fileMenu.add_command(label="oh oh")

fileMenu.add_separator()

fileMenu.add_command(label="exit")

menuBar.add_cascade(label="1  ",menu=fileMenu)

fileMenu2 = tk.Menu(menuBar,tearoff=False)

fileMenu2.add_command(label="game")

fileMenu2.add_command(label="draw")

fileMenu2.add_separator()

subMenu = tk.Menu(menuBar,tearoff=False)

subMenu.add_command(label="max")

subMenu.add_command(label="open")

fileMenu2.add_cascade(label="yo", menu=subMenu)

menuBar.add_cascade(label="2",menu=fileMenu2)

window.config(menu=menuBar)
window.mainloop()
radio5.pack()

window.mainloop()   
    