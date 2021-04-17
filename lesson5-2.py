# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:22:22 2021

@author: Admin
"""

import tkinter as tk

window = tk.Tk()

window.title("youtube下載器")
window.geometry("500x150")
window.resizable(False, False)

onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window, text = "只有音樂", variable = onlyMusic,
                       onvalue = True, offvalue = False)
check.pack()

window.mainloop()


