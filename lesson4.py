# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:11:16 2021

@author: Admin
"""

from pytube import YouTube
import tkinter as tk

progress = 0

def showProgress(stream,chunk,bytes_remaining):
    size =  stream.filesize
    global progress
    preProgress = progress
    currentProgress = (size - bytes_remaining)*100 // size
    progress = currentProgress
    
    if progress == 100:
        print("下載完成")   
        return
    
    if preProgress != progress:
        scale.set(progress)
        window.update
        print("目前進度:" + str(progress) + "%")
        
def onClick():
    
    global var
    var.set(entry.get())
    try:
        yt = YouTube(var.get(),
                     on_progrress_callback = showProgress)
        stream = yt.streams.first()
        stream.download()
    except:
        print("下載失敗")
    
    
window = tk.Tk()
window.title("youtube下載器")
window.geometry("500x150")
window.resizable(False, False)

label = tk.Label(window, text = "請輸入網址")
label.pack()

var = tk.StringVar()
entry = tk.Entry(window, width = 50)
entry.pack()

button = tk.Button(window, text = "下載",
                   command = onClick)
button.pack()
scale = tk.Scale(window, label = '進度條',
                 orient = tk.HORIZONTAL,
                 from_ = 0, to = 100,
                 length = 200,
                 showvalue = False,
                 tickinterval = 0)

scale.pack()

window.mainloop()