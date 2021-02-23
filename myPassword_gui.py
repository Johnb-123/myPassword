# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:56:37 2021

@author: John Byrne

GUI
"""

import re
from tkinter import * 
from tkinter import messagebox
import tkinter as tk


window = Tk()
window.title("Create a username and password")

#Labels
name = Label(window, text="Username")
passwd = Label(window, text="Password")

name_var=StringVar()
passwd_var=StringVar()

#Entry windows for text input
entry = Entry(window, show='*', textvariable=passwd_var)
entry2 = Entry(window, textvariable=name_var)

#GRIDS
name.grid(row=0)
passwd.grid(row=1)
entry.grid(row=1, column=1)
entry2.grid(row=0, column=1)

def submit():
    u_name=name_var.get()
    password=passwd_var.get()
    
    print("Your Username is {} ".format(name))
    print("Your password is {} ".format(password))
    
    name_var.set("")
    passwd_var.set("")
    
def invalid():
    invalid = Tk()
    invalid.title("Invalid Password")
    T = tk.Text(invalid, height=10, width=50)
    T.pack()
    T.insert(tk.END, """Invalid Password/n Include characters:
             numbers
             lowercase
             UPPERCASE
             Special Characters""")
    
def validate():
    while True:
        password=passwd_var.get()
        if password < '8':
            invalid()
            break 
        elif re.search('[0-9]',password) is None:
            invalid()
            break 
        elif re.search('[A-Z]',password) is None: 
            invalid()
            break 
        else:
            window2 = Tk()
            window2.title("Confirmation")
            T = tk.Text(window2, height=2, width=30)
            T.pack()
            T.insert(tk.END, "Your Username and Password\nhas been set")
            break
            
button = Button(text='Validate')
button['command'] = validate
button.grid(row=1, column=3)
window.mainloop()




