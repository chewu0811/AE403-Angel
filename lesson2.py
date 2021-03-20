# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:33:32 2021

@author: Admin
"""

import tkinter as tk

window = tk.Tk()

window.title("Menu")

window.geometry("500x500")

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