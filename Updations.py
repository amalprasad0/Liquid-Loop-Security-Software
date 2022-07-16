

from email.mime import image
from fileinput import close
from pathlib import Path
from re import T
from tkinter import *
from tkinter import ttk
import app

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk,Canvas, Entry, Text, Button, PhotoImage

from numpy import record


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





update_section=Tk()
update_section.configure(bg = "#FFFFFF")
update_section.geometry("960x620")
update_section.wm_title("Record Updation -1")

u_date=StringVar()
u_num=StringVar()
up_name=StringVar()
up_num=StringVar()
up_mob=StringVar()
# methods->
def clicked_up(e):
    set_value()
def updateData():
    date=u_date.get()
    vnum=u_num.get().upper()
    for record in treev.get_children():
        treev.delete(record)
    
    print("Function called")
    filereader=open("Data Records/Vehicle.txt","r")
    lines=filereader.readlines()
    temp=[]
    for line in lines:
        if line.startswith(date):
            if line.find(vnum):
                nl=line.split("|")
                temp.append(nl)
                print(temp)
        else:
            print("line Not Found ")
    if(u_num=="" and date==""):
        print("not found!")
    else:
        for i in range(0,len(temp)):
           treev.insert("", 'end', text ="L"+str(i),values =(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6],temp[i][7]))
           
    filereader.close()

def set_value():
    
     record=treev.focus()
     temp=treev.item(record,'values')
     temp_list=list(temp)
     
     up_name.set(temp_list[4])
     up_num.set(temp_list[2])
     up_mob.set(temp_list[5])
     return temp_list

def update():
    u_name=up_name.get()
    u_num=up_num.get()
    u_mob=up_mob.get()
    temp_list=set_value()
    print("up",temp_list)
    temp_list[7]=temp_list[7]+"\n"
    filereader=open("Data Records/Vehicle.txt","r")
    lines=filereader.readlines()
    temp=[]
    for line in lines:
        if line.startswith(temp_list[0]):
                nl=line.split("|")
                if nl[1]==temp_list[1]:
                    print("up to",nl)
    up_record=[]
    up_record.append(nl[0])
    up_record.append(nl[1])
    up_record.append(u_num)
    up_record.append(nl[3])
    up_record.append(u_name)
    up_record.append(u_mob)
    up_record.append(nl[6])
    up_record.append(nl[7])
    print("up record:",up_record)
    
    update_file="|".join(up_record)
    # print(update_file)

    INDEX=lines.index(line)
    lines[INDEX]=update_file
    print(lines)
    
    filereader2=open("Data Records/Vehicle.txt","w+")
    for i in lines:
        filereader2.write(i)
    filereader2.close()


                    

    
    
    # print("Up:",temp)
    
# date of vhl
vdate = Entry(update_section,
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=u_date
)
vdate.place(
    x=20.0,
    y=100.0,
    width=182.0,
    height=48.0
)

# vhl number
vhlnum = Entry(update_section,
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
addbtn = Button(
    update_section,
    borderwidth=0,
    highlightthickness=0,
    command=updateData,
    relief="flat",
    text="UPDATE"
)
addbtn.place(
    x=470.0,
    y=100.0,
    width=100.0,
    height=50.0
)
# vhl owner name
u_name = Entry(update_section,
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=up_name
)
u_name.place(
    x=20.0,
    y=480.0,
    width=182.0,
    height=48.0
)
# Vehicle number
vhlnum = Entry(update_section,
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=up_num
)
vhlnum.place(
    x=250.0,
    y=480.0,
    width=182.0,
    height=48.0
)
mob = Entry(update_section,
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=up_mob
)
mob.place(
    x=470.0,
    y=480.0,
    width=182.0,
    height=48.0
)
updatebtn = Button(update_section,
    
    borderwidth=0,
    highlightthickness=0,
    command=update,
    relief="flat",
    text="UPDATE"
)
updatebtn.place(
    x=700.0,
    y=480.0,
    width=100.0,
    height=50.0
)
# table->
treev = ttk.Treeview(update_section, selectmode ='browse')
treev.place(x=20,y=220)
    

                    
treev["columns"] = ("1", "2", "3","4","5","6","7","8")
treev['show'] = 'headings'
treev.column("1", width = 100, anchor ='c')
treev.column("2", width = 100, anchor ='se')
treev.column("3", width = 100, anchor ='se')
treev.column("4", width = 100, anchor ='se')
treev.column("5", width = 100, anchor ='se')
treev.column("6", width = 100, anchor ='se')
treev.column("7", width = 100, anchor ='se')
treev.column("8", width = 100, anchor ='se')
treev.bind('<ButtonRelease-1>',clicked_up)                   
treev.heading("1", text ="DATE")
treev.heading("2", text ="TIME")
treev.heading("3", text ="VEHICLE NUMBER")
treev.heading("4", text ="IN/OUT")
treev.heading("5", text ="OWNER NAME")
treev.heading("6", text ="MOBILE")
treev.heading("7", text ="TYPE")
treev.heading("8", text ="REASON")







from time import strftime
from tkinter.ttk import * 
menubar = Menu(update_section)

# file = Menu(update_section, tearoff = 0)
# update_section.add_cascade(label ='File', menu = file)
# file.add_command(label ='New File', command = None)
# file.add_command(label ='Open...', command = None)
# file.add_command(label ='Save', command = None)
# file.add_separator()
# file.add_command(label ='Exit', command = update_section.destroy)



edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
update_section.config(menu = menubar)
update_section.mainloop()




# window.geometry("1493x950")