#!/bin/env python3

from tkinter import *
from tkinter import messagebox
import sys, os
from turtle import left


#================
#= Setup Window =
#================
root = Tk()
root.title("Login Form")
root.resizable(False,False)
root.geometry('800x450+290+150')

#=================
#= Functions All =
#=================
def get_exit():
    exit =  messagebox.askyesno('Exit', 'Do you want to close program')
    if exit == True:
        root.quit()
    elif exit == False:
        pass
    else:
        messagebox.showerror('error', 'something went wrong!')

def get_msg():
    messagebox.showinfo('About','\n[code]BOX | Andrei A. Abd\n')

def login():
    username = user_name_entry.get()
    password = password_entry.get()
    if username == "codeBOX" and password == "@123@123":
        messagebox.showinfo('Warning', 'Hello ' + str(username))
    else:
        messagebox.showerror('Error', 'Uncorrect!')

#==================
#= Style Elements =
#==================
session_1 = Frame(
    root, 
    width=230, 
    height=450, 
    bg='#888',
    borderwidth=1,
    relief="raised"
    )

pragraph_1_session_1 = Label(
    session_1, 
    text='Login Form:', 
    bg='#888', 
    fg='#fff', 
    font=('tajawal', 13, 'bold'),
    justify='center'
    )

pragraph_2_session_1 = Label(
    session_1, 
    text='''Written with python - tkinter library.\nFor successful access read:\nREADME.md on github.

Usage:
type correct user name and password\nclick on Login button to check resulte.''', 
    bg='#888', 
    fg='#fff', 
    font=('tajawal', 8),
    justify='left'
    )

button_1_session_1 = Button(
    session_1, 
    text='Login', 
    width=16, 
    fg='#fff', 
    bg='#666', 
    font=('tajawal', 10, 'bold'),
    command=login
    )

button_2_session_1 = Button(
    session_1, 
    text='About', 
    width=16, 
    fg='#fff', 
    bg='#666', 
    font=('tajawal', 10, 'bold'),
    command = get_msg
    )

button_3_session_1 = Button(
    session_1, 
    text='Exit', 
    width=16, 
    fg='#fff', 
    bg='#666', 
    font=('tajawal', 10, 'bold'),
    command= get_exit
    )

login_frame = Frame(
    width=370, 
    height=105,
    bg='#999',
    borderwidth=1,
    relief="raised"
    )

login_frame_username = Label(
    text='User', 
    fg='#222',
    font=('tajawal', 15),
    bg='#999'
    )

user_name_entry = Entry(
    root, 
    font=('tajawal')
    )

password_entry = Entry(
    root, 
    font=('tajawal')
    )

login_frame_password = Label(
    text='Pssoword', 
    fg='#222',
    font=('tajawal', 15), 
    bg='#999',
    )

footer_main = Label(
    text='[code]Box | Andrei A. Abd | 1993 - 2022', 
    bg='#888', 
    fg='#222', 
    font=('tajawal', 7, 'bold')
    )
#===========================
#= Setup Elements Poistion =
#===========================
session_1.place(x=0,y=0)
pragraph_1_session_1.place(x=0, y=48)
pragraph_2_session_1.place(x=0, y=80)
button_1_session_1.place(x=16, y=220)
button_2_session_1.place(x=16, y=268)
button_3_session_1.place(x=16, y=316)
login_frame.place(x=330, y=180)
login_frame_username.place(x=340, y=193)
user_name_entry.place(x=480, y=193)
login_frame_password.place(x=340, y=250)
password_entry.place(x=480, y=250)
footer_main.place(x=10, y=430)

#===============
#= Run Resulte =
#===============
if __name__ == '__main__':
    root.mainloop()
