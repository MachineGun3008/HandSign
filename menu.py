                                #################
                                # Run This File #
                                #################

import tkinter as tk
from Number import Number
from VideoStream import VideoStream
from Sentence import Sentence
from CommonSentence import CommonSentence
import os

root = tk.Tk()
root.title('Hand sign')
canvas = tk.Canvas(root, width = 400, height = 250)
canvas.pack()
entry = tk.Entry(root)

canvas.create_window(100,100,window = entry, width = 190)
CS = CommonSentence()
S = Sentence()
N = Number()
vd = VideoStream()
paths = []
v = ""

def get_text():
    global v
    v = entry.get()
    global label
    label = tk.Label(root, text = v)
    canvas.create_window(100, 150, window = label)
    paths = CS.FindPath(v)

    if paths != None:
        vd.DisplayVideo(paths)
    else:
        paths = S.FromTextToVid(v)
        vd.DisplayVideo(paths)
    return v

def show_again():
    paths = CS.FindPath(v)
    if paths != None:
        vd.DisplayVideo(paths)
    else:
        paths = S.FromTextToVid(v)
        vd.DisplayVideo(paths)

def input_again():
    entry.delete(0, 'end')
    label.destroy()
    

button = tk.Button(text='Enter', command = lambda: v == get_text(), width=20, fg = 'green',bg = '#C0C0C0')
canvas.create_window(300, 100, window=button)
button_next = tk.Button(text='Next', width=20, command = input_again, fg = 'green',bg = '#C0C0C0')
canvas.create_window(300, 50, window=button_next)
button_relay = tk.Button(text='Replay', width=20, command = show_again, fg = 'green',bg = '#C0C0C0')
canvas.create_window(300, 150, window=button_relay)



root.mainloop()