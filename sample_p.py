from  tkinter import *

from time import strftime

root=Tk()
root.geometry("400x400")

u_num=StringVar()
def time():
    string = strftime('%H:%M:%S %p')
    # vhlnum.config(text = string)
    u_num.set(string)
    vhlnum.after(1000, time)

vhlnum = Entry(root,
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=u_num
        
    )
vhlnum.place(
        x=250.0,
        y=100.0,
        width=182.0,
        height=48.0
    )
time()
root.mainloop()