from tkinter import Tk
from tkinter import Label
import time
import sys


window = Tk()
window.title("Alarm Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(window, font=('Calibri', 90),background="black",foreground="white")
clock.pack()

get_time()

window.mainloop()