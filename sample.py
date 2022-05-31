from email.mime import image
from fileinput import close
from pathlib import Path
from re import T
from tkinter import *
from tkinter import ttk


window=Tk()
window.geometry("400x400")
vhlnum = Entry(window,
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=""
)
vhlnum.place(
    x=100.0,
    y=200.0,
    width=182.0,
    height=48.0
)
updatebtn = Button(window,
    
    borderwidth=0,
    highlightthickness=0,
    command="",
    relief="flat",
    bg="light blue",
    text="UPDATE"
)
updatebtn.place(
    x=0.0,
    y=0.0,
    width=100.0,
    height=50.0
)
window.mainloop()