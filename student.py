

from email.mime import image
from fileinput import close
from pathlib import Path
from re import T
from tkinter import *
from tkinter import ttk


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk,Canvas, Entry, Text, Button, PhotoImage

from numpy import record


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





Supdate_section=Tk()
Supdate_section.configure(bg = "#FFFFFF")
Supdate_section.geometry("960x620")
Supdate_section.wm_title("Student Record Updation")

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
    for record in up_treev.get_children():
        up_treev.delete(record)
    
    print("Function called")
    filereader=open("Data Records/Student.txt","r")
    lines=filereader.readlines()
    temp=[]
    for line in lines:
        if line.startswith(date):
                nl=line.split("|")
                temp.append(nl)
                print(temp)
    for j in range(0,len(temp)):
        if temp[j][3]==vnum:
                print(temp[j])
                up_treev.insert("", 'end', text ="L"+str(j),values =(temp[j][0],temp[j][1],temp[j][2],temp[j][3],temp[j][4],temp[j][5],temp[j][6]))
            
    #     else:
    #         print("line Not Found ")
    # if(u_num=="" and date==""):
    #     print("not found!")
    # else:
    #     for i in range(0,len(temp)):
    #        up_treev.insert("", 'end', text ="L"+str(i),values =(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6]))
           
    filereader.close()

def set_value():
    
     record=up_treev.focus()
     temp=up_treev.item(record,'values')
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
vdate = Entry(Supdate_section,
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
vhlnum = Entry(Supdate_section,
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
    Supdate_section,
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
u_name = Entry(Supdate_section,
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
vhlnum = Entry(Supdate_section,
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
mob = Entry(Supdate_section,
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
updatebtn = Button(Supdate_section,
    
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
up_treev = ttk.Treeview(Supdate_section, selectmode ='browse')
up_treev.place(x=20,y=220)
    

                    
up_treev["columns"] = ("1", "2", "3","4","5","6","7")
up_treev['show'] = 'headings'
up_treev.column("1", width = 100, anchor ='c')
up_treev.column("2", width = 100, anchor ='se')
up_treev.column("3", width = 100, anchor ='se')
up_treev.column("4", width = 100, anchor ='se')
up_treev.column("5", width = 100, anchor ='se')
up_treev.column("6", width = 100, anchor ='se')
up_treev.column("7", width = 100, anchor ='se')

up_treev.bind('<ButtonRelease-1>',clicked_up)                   
up_treev.heading("1", text ="DATE")
up_treev.heading("2", text ="TIME")
up_treev.heading("3", text ="NAME")
up_treev.heading("4", text ="USN")
up_treev.heading("5", text ="IN/OUT")
up_treev.heading("6", text ="MOBILE")
up_treev.heading("7", text ="REASON")










# file = Menu(update_section, tearoff = 0)
# update_section.add_cascade(label ='File', menu = file)
# file.add_command(label ='New File', command = None)
# file.add_command(label ='Open...', command = None)
# file.add_command(label ='Save', command = None)
# file.add_separator()
# file.add_command(label ='Exit', command = update_section.destroy)




Supdate_section.mainloop()




# window.geometry("1493x950")