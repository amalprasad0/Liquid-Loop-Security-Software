
from time import strftime
from email.mime import image
from operator import index
from pathlib import Path
import pandas as pd
from tkinter import ttk
from datetime import date
from datetime import datetime
from time import strftime
import os

from twilio.rest import Client

from tkinter import messagebox
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import bgcolor, color




def vhlview()  :
    view=Tk()
    # window_width = screen_width * .01
    # window_height = screen_height * .04
    # view.geometry("%dx%d" % (window_width,window_height))
    view.geometry("700x400")
    view.title("View Records")
    view.configure(background='#FFFFFF')

    treev = ttk.Treeview(view, selectmode ='browse')
    treev.place(x=0,y=0)
            

                            
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
    filereader=open("Data Records/Vehicle.txt","r")
    lines=filereader.readlines()
    temp=[]
    for line in lines:
                nl=line.split("|")
                temp.append(nl)
            
    for i in range(0,len(temp)):
            
                treev.insert("", 'end', text ="L"+str(i),values =(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6],temp[i][7]))
    view.resizable(False,False)
    view.mainloop()
def studentview():
    view=Tk()
   
    view.geometry("700x600")
    view.title("View Records")
    view.configure(background='#FFFFFF')

    treev = ttk.Treeview(view, selectmode ='browse')
    treev.place(x=0,y=0)
            

                            
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
    treev.heading("3", text ="NAME")
    treev.heading("4", text ="USN")
    treev.heading("5", text ="MOBILE")
    treev.heading("6", text ="IN/OUT")
    treev.heading("7", text ="REASON")
   
    filereader=open("Data Records/Student.txt","r")
    lines=filereader.readlines()
    temp=[]
    for line in lines:
                nl=line.split("|")
                temp.append(nl)
    for i in range(0,len(temp)):
            treev.insert("",'end',text="L"+str(i),values=(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6]))
    view.resizable(False,False)
    view.mainloop()
def lateview():



    
   
    view=Tk()
    view.geometry("700x400")
    view.title("View Records")
    view.configure(background='#FFFFFF')

    treev = ttk.Treeview(view, selectmode ='browse')
    treev.place(x=0,y=0)
            

                            
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
    treev.heading("3", text ="NAME")
    treev.heading("4", text ="USN")
    treev.heading("5", text ="MOBILE")
    treev.heading("6", text ="IN/OUT")
    treev.heading("7", text ="REASON")
   
    filereader=open("Data Records/Late.txt","r")
    lines=filereader.readlines()
    temp=[]
    for line in lines:
                nl=line.split("|")
                temp.append(nl)
    for i in range(0,len(temp)):
            treev.insert("",'end',text="L"+str(i),values=(temp[i][0],temp[i][1],temp[i][2],temp[i][3],temp[i][4],temp[i][5],temp[i][6]))
    
    


    def sendData():
            client = Client('AC791491b32b210bdf650309f0338bb88f', 'efd47247cbe0e4982eca2cc56f93ab58')
            message = client.messages.create(
                        body="Late Commer's Entry :https://docs.google.com/spreadsheets/d/1VRVJkWtozhM3ckA2ujhtS4s7PCrt0YpvwiP_zrisKvU/edit?usp=sharing",
                        from_='+12058915189',
                        to="+918078075784"
                    )

            print(message.sid)
    addbtn = Button(view,
    text ="Send report to CA",
    borderwidth=0,
    bg='#1053FF',
    fg='#FFFFFF',
    highlightthickness=0,
    command=sendData,
    relief="flat"
    )
    addbtn.place(
    x=10.0,
    y=320.0,
    width=210.0,
    height=50.0
    )

    


    
    
    view.mainloop()
websites = pd.read_csv("./Data Records/Clate.txt",header = None)
websites.columns = ['Date', 'Time', 'Name', 'USN', 'Mobile']
websites.to_csv('GeeksforGeeks.csv', index = None)
