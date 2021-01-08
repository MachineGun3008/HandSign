import tkinter as tk
from Number import Number
from VideoStream import VideoStream
from Sentence import Sentence
from CommonSentence import CommonSentence
import os

root = tk.Tk()
canvas = tk.Canvas(root, width = 400, height = 250)
canvas.pack()
entry = tk.Entry(root)

canvas.create_window(100,100,window = entry, width = 190)
def get_text():
    v = entry.get()
    label = tk.Label(root, text = v)
    canvas.create_window(100, 150, window = label)
    


button = tk.Button(text='Enter', command = get_text, width=20)
canvas.create_window(300, 100, window=button)
button_next = tk.Button(text='Next', width=20)
canvas.create_window(300, 50, window=button_next)
button_relay = tk.Button(text='Relay', width=20)
canvas.create_window(300, 150, window=button_relay)



root.mainloop()