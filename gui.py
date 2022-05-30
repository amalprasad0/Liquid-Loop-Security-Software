


from email.mime import image
from pathlib import Path
from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime


from tkinter import messagebox
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import bgcolor




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
# window.geometry("1493x950")
window.state('zoomed')
window.configure(bg = "#FFFFFF")
# -----------------------------------------------Vehicle Section------------------------------------------------#
# Variables for Vehicle record inserition
vlDate=StringVar()
vlTime=StringVar()
vlNum=StringVar()
vlInout=StringVar()
vlOwner=StringVar()
vlMob=StringVar()
vlType=StringVar()
vlReason=StringVar()
# End

# Date->
today = date.today()
vlDate.set(today)
# end
# time->


now = datetime.now()
time = now.strftime("%H:%M:%S")
vlTime.set(time)
# method for Insertion of vhl rcd
def insertData():
    time=vlTime.get()
    date=vlDate.get()
    vehiclenum=vlNum.get()
    Vinout=vlInout.get()
    Vowner=vlOwner.get()
    Vlmob=vlMob.get()
    vltyp=vlType.get()
    vreason=vlReason.get()
    print("Details:",time,"|",date,"|",vehiclenum,"|",Vinout,"|",Vowner,"|",Vowner,"|",Vlmob,"|",vltyp,"|",vreason)
    VhlReader=open("Data Records/Vehicle.txt","a")
    VhlReader.write(date+"|"+time+"|"+vehiclenum+"|"+Vinout+"|"+Vowner+"|"+Vlmob+"|"+vltyp+"|"+vreason+"\n")
    VhlReader.close()
# variables for vhl search->
s_date=StringVar()
s_num=StringVar()
# search method for vehicle
def vehlsearch():
    date=s_date.get()
    print(date)
    vnum=s_num.get().upper()
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
    if(s_num=="" and date==""):
        print("not found!")
    else:
        for i in range(0,len(temp)):
           treev.insert("", 'end', text ="L"+str(i),values =(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6],temp[i][7]))
           
    filereader.close()
    exit

# methed for removal
    # Variable for removal
def removeData():
    record=treev.focus()
    temp=treev.item(record,'values')
    temp_list=list(temp)
    print(temp_list)
    fileReader=open("Data Records/Vehicle.txt","r")
    lines=fileReader.readlines()
    for line in lines:
        del_list=line.split("|")
        if del_list==temp_list:
            print(del_list)
            del lines[lines.index(line)]
            break
    fileReader2=open("Data Records/Vehicle.txt","w+")
    for i in lines:
        fileReader2.write(i)
    selected_item=treev.selection()[0]
    treev.delete(selected_item)
# Update section implemention->

    
    # ended


# ----------------------------------------------------------Student Section------------------------------------------------#

s_time=StringVar()
s_name=StringVar()
s_usn=StringVar()
s_mob=StringVar()
s_reason=StringVar()
s_inout=StringVar()
# Method for insertion od data
         

def studentadd():
    time=s_time.get()
    t_date=date.today()
    name=s_name.get()
    usn=s_usn.get()
    mobile=s_mob.get()
    reason=s_reason.get()
    inout=s_inout.get()
    if name=="":
        messagebox.showerror("Required", "Name is Empty")
    elif usn=="":
        messagebox.showerror("Required", "USN is Empty")
    elif mobile=="":
        messagebox.showerror("Required", "Mobile  is Empty")
    elif reason=="":
        messagebox.showerror("Required", "Reason is Empty")
    elif inout=="":
        messagebox.showerror("Required", "IN/OUT Field is Empty")
    else:
         print("Details:{",time,"|",t_date,"|",name,"|",usn,"|",mobile,"|",reason,"|",inout,"\n")
         messagebox.showinfo("Status", "Record added Successfully ")




# checking for textbox
def getname():
    global name
    boxname=name.get()
    print("box 1 entered",boxname)
    exit
name=StringVar()
# 



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 950,
    width = 1493,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
# Label for  vhl Date
user_name = Label(window,text = "Date:",bg="#FFFFFF").place(x = 170,y = 130) 
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    273.0,
    183.0,
    image=entry_image_1
)
# date of vhl
vdate = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlDate
)
vdate.place(
    x=182.0,
    y=158.0,
    width=182.0,
    height=48.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    515.0,
    260.0,
    image=entry_image_2
)
# mob of vhl
v_mob = Label(window,text = "Phone:",bg="#FFFFFF").place(x = 413,y = 210)
vmob = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlMob
)
vmob.place(
    x=424.0,
    y=235.0,
    width=182.0,
    height=48.0
)



entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    273.0,
    260.0,
    image=entry_image_3
)
v_name = Label(window,text = "Name:",bg="#FFFFFF").place(x = 173.0,y = 210)

# owner name
vhlowner = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlOwner,
    
)
vhlowner.place(
    x=182.0,
    y=235.0,
    width=182.0,
    height=48.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    515.0,
    183.0,
    image=entry_image_4
)
v_num = Label(window,text = "Vehicle Number:",bg="#FFFFFF").place(x = 413,y = 130) 
# number of vhtl
vlnum = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlNum
)
vlnum.place(
    x=424.0,
    y=158.0,
    width=182.0,
    height=48.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    1521.0,
    54.0,
    fill="#0F52FF",
    outline="")

canvas.create_text(
    632.0,
    13.0,
    anchor="nw",
    text="SECURITY ASSISTANT ",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    81.0,
    183.0,
    image=entry_image_5
)
v_num = Label(window,text = "Time:",bg="#FFFFFF").place(x = 29,y = 130) 
# time
vtime = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlTime
)
vtime.place(
    x=40.0,
    y=158.0,
    width=82.0,
    height=48.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    81.0,
    260.0,
    image=entry_image_6
)
v_name = Label(window,text = "in/out:",bg="#FFFFFF").place(x = 29.0,y = 210)
# inout of vhl
vlinout = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlInout
)
vlinout.place(
    x=40.0,
    y=235.0,
    width=82.0,
    height=48.0
)
v_name = Label(window,text = "Vehicle Type:",bg="#FFFFFF").place(x = 29.0,y = 288)
# type of car

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    81.0,
    337.0,
    image=entry_image_7
)
vtype= Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlType
)
vtype.place(
    x=40.0,
    y=312.0,
    width=82.0,
    height=48.0
)
v_name = Label(window,text = "Reason:",bg="#FFFFFF").place(x = 173.0,y = 288)
# Reson Vehile
entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    273.0,
    337.0,
    image=entry_image_8
)
vhlreason = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=vlReason
)
vhlreason.place(
    x=182.0,
    y=312.0,
    width=182.0,
    height=48.0
)
# Add Button

button_image_1 = PhotoImage(
    file=relative_to_assets("ADD.png"))
addbtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=insertData,
    relief="flat"
)
addbtn.place(
    x=410.0,
    y=312.0,
    width=210.0,
    height=50.0
)
# Vehicle Record Adding Section Complted

# ----------------------------------------Student Details Adding Section-------------------------------------->

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    273.0,
    491.0,
    image=entry_image_9
)
# Name for student
student_Name = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_name
)
student_Name.place(
    x=182.0,
    y=466.0,
    width=182.0,
    height=48.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    515.0,
    568.0,
    image=entry_image_10
)
# Reason For student S
student_Reason = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_reason
)
student_Reason.place(
    x=424.0,
    y=543.0,
    width=182.0,
    height=48.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    273.0,
    568.0,
    image=entry_image_11
)
# Student mobile S
student_mob = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_mob
)
student_mob.place(
    x=182.0,
    y=543.0,
    width=182.0,
    height=48.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    515.0,
    491.0,
    image=entry_image_12
)
# USN 
usn_S = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_usn
)
usn_S.place(
    x=424.0,
    y=466.0,
    width=182.0,
    height=48.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    81.0,
    491.0,
    image=entry_image_13
)
# Time for Student S
student_Time = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_time
)
student_Time.place(
    x=40.0,
    y=466.0,
    width=82.0,
    height=48.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    81.0,
    568.0,
    image=entry_image_14
)
# IN Or OUT for Student S
inout_s = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_inout
)
inout_s.place(
    x=40.0,
    y=543.0,
    width=82.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("ADD.png"))
s_addbtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=studentadd,
    relief="flat"
)
s_addbtn.place(
    x=410.0,
    y=620.0,
    width=210.0,
    height=50.0
)


# jhfkgjgf
entry_image_20 = PhotoImage(
    file=relative_to_assets("TextBox.png"))
entry_bg_20 = canvas.create_image(
    770.0,
    176.0,
    image=entry_image_20
)
vsearch_date = Label(window,text = "Date:",bg="#FFFFFF").place(x = 665,y = 127) 
vs_date = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_date
    
)
vs_date.place(
    x=675.0,
    y=152.0,
    width=192.0,
    height=48.0
)
# ended
# vs_num
entry_image_21 = PhotoImage(
    file=relative_to_assets("TextBox.png"))
entry_bg_21 = canvas.create_image(
    1070.0,
    176.0,
    image=entry_image_21
)
vsearch = Label(window,text = "Vehicle Number:",bg="#FFFFFF").place(x = 965,y = 127) 
vs_num = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=s_num
    
)
vs_num.place(
    x=975.0,
    y=152.0,
    width=188.0,
    height=48.0
)
# ended
# Search button
button_image_21 = PhotoImage(
    file=relative_to_assets("SEARCH.png"))
v_searchbtn = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=vehlsearch,
    relief="flat"
)
v_searchbtn.place(
    x=1250.0,
    y=152.0,
    width=210.0,
    height=50.0
)




# Treeview->
treev = ttk.Treeview(window, selectmode ='browse')
treev.place(x=670,y=220)
    

                    
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
                    
treev.heading("1", text ="DATE")
treev.heading("2", text ="TIME")
treev.heading("3", text ="VEHICLE NUMBER")
treev.heading("4", text ="IN/OUT")
treev.heading("5", text ="OWNER NAME")
treev.heading("6", text ="MOBILE")
treev.heading("7", text ="TYPE")
treev.heading("8", text ="REASON")

# # ended-<

# Button For removal
button_image_22 = PhotoImage(
    file=relative_to_assets("REMOVE.png"))
v_removetn = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=removeData,
    relief="flat"
)
v_removetn.place(
    x=1250.0,
    y=460.0,
    width=210.0,
    height=50.0
)
def update():
    exec(open("update.py").read())
menubar = Menu(window,background='blue')
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Updations', menu = edit)
edit.add_command(label ='Vehicle Record Updation', command =update)
edit.add_command(label ='Student Record Updation', command = "")



help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help)
help.add_command(label ='Any TroubleShoot?', command = "")
help.add_command(label ='Report Issue', command = "")
help.add_command(label ='Contact us', command = "")

Contribute = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Open Sourse',menu=Contribute)
menubar.add_command(label ='Get me to Repo',command="" )
menubar.add_command(label ='Donate',command="")

about = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='More', menu = about)
about.add_command(label ='About Developer', command = "")
about.add_command(label ='Version', command = "")
about.add_command(label ='Check for update', command = "")


window.config(menu = menubar)

u_date=StringVar()
u_num=StringVar()
up_name=StringVar()
up_num=StringVar()
up_mob=StringVar()
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()
window.resizable(False,False)
# window.attributes('-fullscreen', True)
window.mainloop()
