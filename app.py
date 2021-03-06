

import webbrowser as wb
from view import vhlview,studentview,lateview
from time import strftime
from email.mime import image
from operator import index
from pathlib import Path
from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
from time import strftime
import os
from twilio.rest import Client
import webbrowser as wb
from menus1 import *
from tkinter import messagebox
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import bgcolor, color




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

wb.register('chrome', None)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1493x950")
# window.state('zoomed')
window.wm_title("Liquid-Loop SECURITY ASSISTANT")
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

def time():
    string = strftime('%I:%M:%S %p')
    
    
    vlTime.set(string)
    vdate.after(1000, time)
    
# method for Insertion of vhl rcd
def insertData():
    time=vlTime.get()
    date=vlDate.get()
    vehiclenum=vlNum.get().upper()
    Vinout=vlInout.get().upper()
    Vowner=vlOwner.get().upper()
    Vlmob=vlMob.get().upper()
    vltyp=vlType.get().upper()
    vreason=vlReason.get().upper()
    if vehiclenum=="":
        messagebox.showwarning("showwarning", "Field Is Empty")
    elif Vinout=="":
        messagebox.showwarning("showwarning", "Field Is Empty")
    elif Vowner=="":
        messagebox.showwarning("showwarning", "Field Is Empty")
    elif Vlmob=="":
        messagebox.showwarning("showwarning", "Field Is Empty")
    elif vltyp=="":
        messagebox.showwarning("showwarning", "Field Is Empty")
    elif vreason=="":
        messagebox.showwarning("showwarning", "Field Is Empty")
    else:
        print("Details:",time,"|",date,"|",vehiclenum,"|",Vinout,"|",Vowner,"|",Vowner,"|",Vlmob,"|",vltyp,"|",vreason)
        VhlReader=open("Data Records/Vehicle.txt","a")
        VhlReader.write(str(date)+"|"+time+"|"+vehiclenum+"|"+Vinout+"|"+Vowner+"|"+Vlmob+"|"+vltyp+"|"+vreason+"\n")
        messagebox.showinfo("STATUS", "RECORD ADDED TO DATABASE")
        
           
        # client = Client('AC4fb3f859d841739f658840ac79a3e879', '6bbdad1b6761f73b391dae6b4c69f87f')
        # message = client.messages \
        #         .create(
        #              body="Hi "+Vowner+"Welcome to Yenepoya Institute of Technology"+" \nYour entering Time :"+str(time)+"\nDate:"+str(date)+"\nVehicle Number:"+vehiclenum+"\nLiqiud-Loop Gate Security System",
        #              from_='+19403505053',
        #              to="+91"+Vlmob
        #          )

        # print(message.sid)



        VhlReader.close()
# variables for vhl search->
s_date=StringVar()
s_num=StringVar()
# search method for vehicle
def vehlsearch():
    date=s_date.get()
    print(date)
    vnum=s_num.get().upper()
    if(s_num=="" or date==""):
        messagebox.showerror("Required", "Feild is Empty\n Try Again")
    for record in treev.get_children():
        treev.delete(record)
    print("Function called")
    filereader=open("Data Records/Vehicle.txt","r")
    lines=filereader.readlines()
    temp=[]
    for line in lines:
        if line.startswith(date):
            # if line.find(vnum,20,30):
            #     nl=line.split("|")
            #     temp.append(nl)
            #     print(temp)
            nl=line.split("|")
            temp.append(nl)
        
    for i in range(0,len(temp)):
        if temp[i][2]==vnum:
            treev.insert("", 'end', text ="L"+str(i),values =(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6],temp[i][7]))   
        
    # else:
    #     for i in range(0,len(temp)):
    #        treev.insert("", 'end', text ="L"+str(i),values =(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6],temp[i][7]))
           
    filereader.close()
    exit

# methed for removal
    # Variable for removal
def removeData():
    record=treev.focus()
    temp=treev.item(record,'values')
    temp_list=list(temp)
    print(temp_list)
    messagebox.askokcancel("askokcancel", "Want to continue?")
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
# ---------------------------------------UPDATE----------------------------
def update_sec():
    update_section=Toplevel(window)
    update_section.configure(bg = "#FFFFFF")
    update_section.geometry("960x620")
    update_section.wm_title("Record Updation")

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
                        index=lines.index(line)
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

        # INDEX=lines.index(line)
        lines[index]=update_file
        print(lines)

        
        filereader2=open("Data Records/Vehicle.txt","w+")
        for i in lines:
            filereader2.write(i)
        messagebox.showinfo("Sucess", "Successfully updated")
        u_name=up_name.set("")
        u_num=up_num.set("")
        u_mob=up_mob.set("")
        filereader2.close()
        update_section.mainloop()

                        

        
        
        # print("Up:",temp)
        
    # date of vhl
    vdate = Label(update_section,text = "Date:",bg="#FFFFFF").place(x = 20,y = 70)

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
    vhlnum = Label(update_section,text = "Vehicle Number:",bg="#FFFFFF").place(x = 250,y = 70)
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
        text="View"
    )
    addbtn.place(
        x=470.0,
        y=100.0,
        width=100.0,
        height=50.0
    )
    # vhl owner name
    u_name = Label(update_section,text = "Owner:",bg="#FFFFFF").place(x = 20,y = 455)
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
    vhlnum = Label(update_section,text = "Vehicle Number:",bg="#FFFFFF").place(x = 247,y = 455)

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
    mob= Label(update_section,text = "Mobile:",bg="#FFFFFF").place(x = 473,y = 455)
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


# --------------------------------------UPDATE ENDED-----------------------


# ----------------------------------------------------------Student Section------------------------------------------------#

s_time=StringVar()
s_name=StringVar()
s_usn=StringVar()
s_mob=StringVar()
s_reason=StringVar()
s_inout=StringVar()
ss_Date=StringVar()
ss_Usn=StringVar()
# Method for insertion od data
# import time
def ftime():
    string=strftime('%I:%M:%S %p')
    s_time.set(string)
    student_Time.after(1000,ftime)
# t=time.strftime("%I:%M:%S %p")   
# s_time.set(t)
def studentadd():

    time=s_time.get()
    t_date=date.today()
    name=s_name.get().upper()
    usn=s_usn.get().upper()
    mobile=s_mob.get()
    reason=s_reason.get().upper()
    inout=s_inout.get().upper()
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
         stud_file=open("Data Records/Student.txt","a")
         stud_file.write(str(t_date)+"|"+time+"|"+name+"|"+usn+"|"+mobile+"|"+inout+"|"+reason+"\n")
         latefile=open("Data Records/Late.txt","a")
         latef=open("Data Records/Clate.txt","a")
         if(time=='09:00:00 PM'):
            latefile.write(str(t_date)+"|"+time+"|"+name+"|"+usn+"|"+mobile+"|"+inout+"|"+reason+"\n")
            latef.write(str(t_date)+","+time+","+name+","+usn+","+mobile+","+inout+","+reason+"\n")
            messagebox.showwarning("Status", "Record added to late commer's list")
         stud_file.close()
#--------------SEARCH FOR STUD----------  
def searchStudent():
    o_date=ss_Date.get()
    usn=ss_Usn.get().upper()
    studentfile=open("Data Records/Student.txt")
    for record in s_treev.get_children():
        s_treev.delete(record)
    lines=studentfile.readlines()
    match=[]
    for line in lines:
        if line.startswith(o_date):
            if line.find(usn):
                s_line=line.split("|")
                match.append(s_line)
                print(match)
        else:
            print("line not found!")
    if(o_date=="" and usn==""):
        print("Field is empty")
    else:
        for i in range(0,len(match)):
            if match[i][3]==usn:
                
                s_treev.insert("",'end',text="L"+str(i),values=(match[i][0],match[i][1],match[i][2],match[i][3],match[i][4],match[i][5],match[i][6]))
    studentfile.close()

# 
# ---------------Ended------------------------->
# Removal--------------------->
def removeStudent():
    record=s_treev.focus()
    temp=s_treev.item(record,'values')
    temp_list=list(temp)
    print(temp_list)
    fileReader=open("Data Records/Student.txt","r")
    lines=fileReader.readlines()
    for line in lines:
        del_list=line.split("|")
        if del_list==temp_list:
            print(del_list)
            del lines[lines.index(line)]
            break
    fileReader2=open("Data Records/Student.txt","w+")
    for i in lines:
        fileReader2.write(i)
    selected_item=s_treev.selection()[0]
    s_treev.delete(selected_item)

# --------------------ended>

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
    file=("./assets/entry_1.png"))
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
    file=("./assets/entry_2.png"))
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
    file=("./assets/entry_3.png"))
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
    file=("./assets/entry_4.png"))
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
    file=("./assets/entry_5.png"))
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
    file=("./assets/entry_6.png"))
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
    file=("./assets/entry_7.png"))
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
    file=("./assets/entry_8.png"))
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
    file=("./assets/ADD.png"))
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
    file=("./assets/entry_9.png"))
entry_bg_9 = canvas.create_image(
    273.0,
    491.0,
    image=entry_image_9
)
# Name for student
S_NAME = Label(window,text = "Name:",bg="#FFFFFF").place(x = 173.0,y = 440)
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
    file=("./assets/entry_10.png"))
entry_bg_10 = canvas.create_image(
    515.0,
    568.0,
    image=entry_image_10
)
S_REASON = Label(window,text = "Reason:",bg="#FFFFFF").place(x = 413,y = 518)
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
    file=("./assets/entry_11.png"))
entry_bg_11 = canvas.create_image(
    273.0,
    568.0,
    image=entry_image_11
)
# Student mobile S
S_MOB = Label(window,text = "Mobile:",bg="#FFFFFF").place(x = 173.0,y = 518)
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
    file=("./assets/entry_12.png"))
entry_bg_12 = canvas.create_image(
    515.0,
    491.0,
    image=entry_image_12
)
# USN 
S_USN = Label(window,text = "USN:",bg="#FFFFFF").place(x = 413,y = 440) 
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
    file=("./assets/entry_13.png"))
entry_bg_13 = canvas.create_image(
    81.0,
    491.0,
    image=entry_image_13
)
# Time for Student S
S_TIME = Label(window,text = "Time:",bg="#FFFFFF").place(x = 29.0,y = 440)
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
    file=("./assets/entry_14.png"))
entry_bg_14 = canvas.create_image(
    81.0,
    568.0,
    image=entry_image_14
)
S_INOUT = Label(window,text = "IN/OUT:",bg="#FFFFFF").place(x = 29.0,y = 518)
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
    file=("./assets/ADD.png"))
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


# Search date vhl----------------------->
entry_image_20 = PhotoImage(
    file=("./assets/TextBox.png"))
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
    file=("./assets/TextBox.png"))
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
    file=("./assets/SEARCH.png"))
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




# Treeview---------------------->
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

# -------------------------- ended-<

# ------------Button For removal-----------------
button_image_22 = PhotoImage(
    file=("./assets/REMOVE.png"))
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
# ------------usn-------->
entry_image_28 = PhotoImage(
    file=("./assets/TextBox.png"))
entry_bg_28 = canvas.create_image(
    1070.0,
    544.0,
    image=entry_image_21
)
st_date = Label(window,text = "USN:",bg="#FFFFFF").place(x = 965,y = 490) 
ss_usn = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=ss_Usn
    
)
ss_usn.place(
    x=975.0,
    y=520.0,
    width=188.0,
    height=48.0
)

# -----------------------ended->
# -------------------------date--------------
entry_image_29 = PhotoImage(
    file=("./assets/TextBox.png"))
entry_bg_20 = canvas.create_image(
    770.0,
    544.0,
    image=entry_image_29
)
ssearch_date = Label(window,text = "Date:",bg="#FFFFFF").place(x = 665,y = 490) 
ss_date = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    textvariable=ss_Date
    
)
ss_date.place(
    x=675.0,
    y=520.0,
    width=192.0,
    height=48.0
)
# ------button for remove ss-------------------->
button_image_30 = PhotoImage(
    file=("./assets/REMOVE.png"))
v_removetn = Button(
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=removeStudent,
    relief="flat"
)
v_removetn.place(
    x=1250.0,
    y=840.0,
    width=210.0,
    height=50.0
)
# --------------------------------------ened-->

# --------------------------------TABLE FOR SYUDENT------------------
s_treev = ttk.Treeview(window, selectmode ='browse')
s_treev.place(x=670,y=600)
    

                    
s_treev["columns"] = ("1", "2", "3","4","5","6","7")
s_treev['show'] = 'headings'
s_treev.column("1", width = 100, anchor ='c')
s_treev.column("2", width = 100, anchor ='se')
s_treev.column("3", width = 100, anchor ='se')
s_treev.column("4", width = 100, anchor ='se')
s_treev.column("5", width = 100, anchor ='se')
s_treev.column("6", width = 100, anchor ='se')
s_treev.column("7", width = 100, anchor ='se')

                    
s_treev.heading("1", text ="DATE")
s_treev.heading("2", text ="TIME")
s_treev.heading("3", text ="NAME")
s_treev.heading("4", text ="USN")
s_treev.heading("5", text ="MOBILE")
s_treev.heading("6", text ="REASON")
s_treev.heading("7", text ="IN/OUT")

# Btn For Student Search
button_image_25 = PhotoImage(
    file=("./assets/SEARCH.png"))
s_searchbtn = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=searchStudent,
    relief="flat"
)
s_searchbtn.place(
    x=1250.0,
    y=520.0,
    width=210.0,
    height=50.0
)
# ---------------------STUDENT update -------------------------------------->
def student_update():
    Supdate_section=Toplevel(window)
    Supdate_section.configure(bg = "#FFFFFF")
    Supdate_section.geometry("960x620")
    Supdate_section.wm_title("Student Record Updation")
    search_date=StringVar()
    search_usn=StringVar()

    sup_name=StringVar()
    sup_usn=StringVar()
    sup_mob=StringVar()
    search_date.set("2022-05-27")
    search_usn.set("4dm19is045")
    def SearchTree():
        Student_date=search_date.get()
        print(Student_date)
        Student_usn=search_usn.get().upper()
        print(Student_usn)
        for record in up_treev.get_children():
            up_treev.delete(record)
        print("Student Function Called:[TreeSearch]")
        searchtreefile=open("Data Records/Student.txt","r")
        datas=searchtreefile.readlines()
        searchTemp=[]
        for line in datas:
            if line.startswith(Student_date):
                    smatch=line.split("|")
                    searchTemp.append(smatch)
                    print("Smatch:",smatch)
        for j in range(0,len(searchTemp)):
            if searchTemp[j][3]==Student_usn:
                print(searchTemp[j])   
                up_treev.insert("", 'end', text ="L"+str(j),values =(searchTemp[j][0],searchTemp[j][1],searchTemp[j][2],searchTemp[j][3],searchTemp[j][4],searchTemp[j][5],searchTemp[j][6]))
            else:
                 print("Not Found")
        searchtreefile.close()
    def set_value():
    
     record=up_treev.focus()
     temp=up_treev.item(record,'values')
     temp_list=list(temp)
     
     sup_usn.set(temp_list[3])
     sup_name.set(temp_list[2])
     sup_mob.set(temp_list[4])
     return temp_list
    def clicked_up(e):
        set_value() 
                      
    # def update_student():
    #     upname=sup_name.get().upper()
    #     upmob=sup_mob.get()
    #     up_usn=sup_usn.get().upper()
    #     temp_list=set_value()
    #     print("For Update List:",temp_list)
    #     stud_file=open("Data Records/Student.txt","r")
    #     lines=stud_file.readline()
    #     up_record1=[]
        
    #     for line in lines:
    #         if line.startswith(temp_list[0]):
    #             nl=line.split("|")
    #             if nl[1]==temp_list[1]:
    #                 print("list:",nl)
        
    #     up_record1.append(nl[0])
    #     up_record1.append(nl[1])
    #     up_record1.append(upname)
    #     up_record1.append(up_usn)
    #     up_record1.append(upmob)
    #     up_record1.append(nl[5])
    #     up_record1.append(nl[6])
    #     print("Updated List:",up_record1)
    #     update_file="|".join(up_record1)
    def update():
        u_name=sup_name.get()
        u_num=sup_usn.get()
        u_mob=sup_mob.get()
        temp_list=set_value()
        print("up",temp_list)
        
        filereader=open("Data Records/Student.txt","r")
        lines=filereader.readlines()
        temp=[]
        for line in lines:
            if line.startswith(temp_list[0]):
               
                    nl=line.split("|")
                    print(line)
                    if nl[2]==temp_list[2]:
                        print("up to",)
                        Index=lines.index(line)
                        print(Index)
            

        up_record=[]
        up_record.append(nl[0])
        up_record.append(nl[1])
        up_record.append(u_name)
        up_record.append(u_num)
        up_record.append(u_mob)
        up_record.append(nl[5])
        up_record.append(nl[6])
        
        print("up record:",up_record)
        
        update_file="|".join(up_record)
        # print(update_file)

        
        lines[Index]=update_file
        print(Index)
        print(lines)
        
        filereader2=open("Data Records/Student.txt","w+")
        for i in lines:
            filereader2.write(i)
        messagebox.showinfo("Status", "Record Updated")
        sup_name.set("")
        sup_usn.set("")
        sup_mob.set("")
        filereader2.close()
# -----------------Endend------------

        
        
        
    # date of Student
    vdate = Label(Supdate_section,text = "Date:",bg="#FFFFFF").place(x = 20,y = 70)

    student_date = Entry(Supdate_section,
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=search_date
    )
    student_date.place(
        x=20.0,
        y=100.0,
        width=182.0,
        height=48.0
    )

    # vhl number
    vhlnum = Label(Supdate_section,text = "USN:",bg="#FFFFFF").place(x = 250,y = 70)

    student_usn = Entry(Supdate_section,
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=search_usn
    )
    student_usn.place(
        x=250.0,
        y=100.0,
        width=182.0,
        height=48.0
    )
    student_btn = Button(
        Supdate_section,
        borderwidth=0,
        highlightthickness=0,
        command=SearchTree,
        relief="flat",
        text="UPDATE"
    )
    student_btn.place(
        x=470.0,
        y=100.0,
        width=100.0,
        height=50.0
    )
    # vhl owner name
    u_name = Label(Supdate_section,text = "Name:",bg="#FFFFFF").place(x = 20,y = 455)

    update_nameS = Entry(Supdate_section,
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=sup_name
    )
    update_nameS.place(
        x=20.0,
        y=480.0,
        width=182.0,
        height=48.0
    )
    # Vehicle number
    vhlnum = Label(Supdate_section,text = "USN:",bg="#FFFFFF").place(x = 247,y = 455)

    student_usn2 = Entry(Supdate_section,
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=sup_usn
    )
    student_usn2.place(
        x=250.0,
        y=480.0,
        width=182.0,
        height=48.0
    )
    mob= Label(Supdate_section,text = "Mobile:",bg="#FFFFFF").place(x = 473,y = 455)
    student_mob= Entry(Supdate_section,
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=sup_mob
    )
    student_mob.place(
        x=470.0,
        y=480.0,
        width=182.0,
        height=48.0
    )
    Supdatebtn = Button(Supdate_section,
        
        borderwidth=0,
        highlightthickness=0,
        command=update,
        relief="flat",
        text="UPDATE"
    )
    Supdatebtn.place(
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
    up_treev.heading("5", text ="MOBILE")
    up_treev.heading("6", text ="IN/OUT")
    up_treev.heading("7", text ="REASON")










    # file = Menu(update_section, tearoff = 0)
    # update_section.add_cascade(label ='File', menu = file)
    # file.add_command(label ='New File', command = None)
    # file.add_command(label ='Open...', command = None)
    # file.add_command(label ='Save', command = None)
    # file.add_separator()
    # file.add_command(label ='Exit', command = update_section.destroy)




    Supdate_section.mainloop()
# --------------------------ENDED-----------------------------------------<

# --------------------ENDED----------------------------------
menubar = Menu(window,background='blue')
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Updations', menu = edit)
edit.add_command(label ='Vehicle Record Updation', command =update_sec)
edit.add_command(label ='Student Record Updation', command = student_update)

view1= Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='View', menu = view1)
view1.add_command(label ='Late Entries', command = lateview)
view1.add_command(label ='View all vehicle records', command =vhlview)
view1.add_command(label ='View all student record', command = studentview)

help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help)
help.add_command(label ='Any TroubleShoot?', command = "")
help.add_command(label ='Report Issue', command = "")
help.add_command(label ='Contact us', command = "")

Contribute = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Repo',menu=Contribute)
Contribute.add_command(label ='Take me to repository',command=lambda:wb.open("https://github.com/amalprasad0/Liquid-Loop-Security-Software"))
Contribute.add_command(label ='Contribute now',command=lambda:wb.open("https://github.com/amalprasad0/Liquid-Loop-Security-Software"))

about = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='More', menu = about)
about.add_command(label ='About Developer', command = lambda:wb.open("https://github.com/amalprasad0"))
about.add_command(label ='Version', command = lambda:wb.open("https://github.com/amalprasad0/Liquid-Loop-Security-Software/releases/tag/v1.0.3"))
about.add_command(label ='Check for update', command = lambda: wb.open("https://github.com/amalprasad0/Liquid-Loop-Security-Software/releases/tag/v1.0.3"))


window.config(menu = menubar)

u_date=StringVar()
u_num=StringVar()
up_name=StringVar()
up_num=StringVar()
up_mob=StringVar()
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()
# ----------------------------bootom tab-------------------->
file = open("Data Records/Student.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
file2 = open("Data Records/Vehicle.txt", "r")
line_count1 = 0
for line in file2:
    if line != "\n":
        line_count1 += 1
file2.close()
tcount=line_count+line_count1


statusbar =Label(window, text="Records:"+str(tcount)+"    Updated Records:7     ????:Live", bd=1, relief=SUNKEN, anchor=W,bg="#0F52FF",fg="#FFFFFF")
statusbar.pack(side=BOTTOM, fill=X)
# ended------------>
window.resizable(False,False)
time()
ftime() 
# ------STUDENT SEARCH SECTION-------->
photo = PhotoImage(file ="assets/barrier.png")
window.iconphoto(False,photo)
window.mainloop()
