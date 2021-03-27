# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:23:31 2021

@author: Admin
"""
from pytube import YouTube

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
        print("目前進度:" + str(progress) + "%")
                                            
yt = YouTube("https://www.youtube.com/watch?v=rAsdsomsKv4",on_progress_callback = showProgress)

stream = yt.streams.filter(res = '360p').first()
#stream = yt.streams.all()
stream.download("video", "Frozen_360p_24fps")