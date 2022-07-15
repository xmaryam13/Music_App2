import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer 
import os
import time


PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox = None
filePathLabel = None

global song_counter
song_counter = 0


for file in os.listdir('shared_files'):
    filename = os.fsdecode(file)
    listbox.insert(song_counter,filename)
    song_counter = song_counter + 1
    
def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)
    
    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()
    if (song_selected != ""):
        infoLabel.configure(text='Now Playing: ' + song_selected)
    else:
        infoLabel.configure(text="")
        

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/', song_selected)
    mixer.music.pause()
    infoLabel.configure(text= "")
    
def resume():
    global song_selected
    
    mixer.init()
    mixer.music.load('shared_files'+song_selected)
    mixer.music.play()
    
def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files'+song_selected)
    mixer.music.pause()



def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry('300x300')
    window.configure(bg = 'LightSkyBlue')
    
    selectLabel = Label(window, text = 'Select Song', bg = 'LightSkyBlue', font = ('Calibri',10))
    selectLabel.place(x=2,y=2)
    
    listBox = Listbox(window, height = 10, width = 39, activestyle = 'dotbox',bg = 'LightSkyBlue', borderwidth = 2, font = ('Calibri',10))
    listBox.place(x=12,y=20)
    
    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight = 1, relx=1)
    scrollbar1.config(command = listBox.yview)
    
    playButton = Button(window, text='Play',width = 10, bd = 1, bg = 'SkyBlue',font = ('Calibri',10),command = play)
    playButton.place(x=30,y=200)
    
    stopButton = Button(window, text='Stop',bd=1,width=10,bg='SkyBlue',font = ('Calibri',10),command = stop)
    stopButton.place(x=200,y=200)
    
    uploadButton = Button(window, text = 'Upload',width = 10, bd = 1, bg = 'SkyBlue',font = ('Calibri',10))
    uploadButton.place(x = 30,y=250)
    
    downloadButton = Button(window, text='Download',width = 10,bd=1,bg='SkyBlue',font=('Calibri',10))
    downloadButton.place(x=200,y=250)
    
    infoLabel = Label(window, text = '',fg = 'blue',font = ('Calibri',10))
    infoLabel.place(x=4,y=200)
    
    ResumeButton = Button(window,text='Resume',width = 10,bd=1,bg='SkyBlue',font=('Calibri',10),command=resume)
    ResumeButton.place(x=50,y=250)
    
    PauseButton = Button(window,text='Pause Button',bd=1,bg='SkyBlue',font=('Calibri',10),command=pause)
    PauseButton.place(x=230,y=250)    
    
    
    window.mainloop()
    

def set_up():
    global SERVER
    global PORT
    global IP_ADDRESS
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    
    musicWindow()
    
set_up()
