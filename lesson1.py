# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:00:33 2021

@author: Admin
"""
import tkinter as tk
import tkinter.messagebox

def ClickMe():
    tkinter.messagebox.showinfo(title = 'hh', message = 'so')
    
window = tk.Tk()
window.title("window")
window.geometry('500x500')

label = tk.Label(window,text="my GUI",bg="#000",fg="#fff")

label.pack()

entry = tk.Entry(window,width = 20)

entry.pack()

button = tk.Button(window,text = "yes",command = ClickMe)

button.pack()

window.mainloop()
