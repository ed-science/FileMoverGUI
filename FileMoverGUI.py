'''Python program to move file from one folder to another folder.
@author : CodePerfectPLus
@language : Python 3
Website : http://codeperfectplus.github.io/
Github : https://github.com/codePerfectPlus
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  

'''
import os
from os import path
from shutil import move
import tkinter as tk


def create_folder():
    paths = ['Moved Python',
        'Moved Picture',
        'Moved Video',
        'Moved Pdf',
        'Moved Music',
        'CodePerfectPlus']
    for root in paths:
        try:  
            os.mkdir(root)  
        except OSError as error:  
            print('Folder Already Exists')
pic = ['.jpeg','.jpg','.png','.gif','.tiff','.raw']
vid = ['.mp4','.webm','.mkv','.MPG', '.MP2', '.MPEG', '.MPE', '.MPV', '.OGG', '.M4P', '.M4V', '.AVI',
 '.WMV', '.MOV', '.QT', '.FLV', '.SWF','.AVCHD']
pytho =['.ipynb','.java']
txt = ['.txt','.pdf']
music = [ '.WAV', '.aif', '.mp3','.mid']
def start():
    for f in os.listdir():
        name , ex = path.splitext(f)
        for i in range(len(pic)):
            if ex == pic[i]:
                move(f,'Moved Picture')
        for i in range(len(vid)):
            if ex == vid[i]:
                move(f,'Moved Video')
        for i in range(len(pytho)):
            if ex == pytho[i]:
                move(f,'Moved Python')
        for i in range(len(txt)):
            if ex == txt[i]:
                move(f,'Moved Pdf')
        for i in range(len(music)):
            if ex == music[i]:
                move(f,'Moved Music')

# Gui        
effects=tk.GROOVE

window = tk.Tk()

frame_a = tk.Frame(master=window,width=80,relief=effects,borderwidth=5)
frame_b = tk.Frame(master=window,width=80,relief=effects,borderwidth=5)

frame_a.grid(row =1, column=1)
frame_b.grid(row=2,column=1)

window.rowconfigure(2,minsize=300,weight=1)
window.columnconfigure(1,minsize=300,weight=1)


btn = tk.Button(master=frame_a,text='Create Folder',command=create_folder,bg='green',width=20,height=5)
btn2 = tk.Button(master=frame_b,text='Move Now',command=start,bg='red',width=20,height=5)
lbl = tk.Label(master=window,text='Warning \n First Create Folder Then Click On Move',fg='red',bg='black',width=50)

lbl.grid(row=0,column=1)
btn.grid(row=1,column=0)
btn2.grid(row=1,column=1)
window.mainloop()