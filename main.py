from tkinter import *
from tkinter import messagebox
import tkinter
import random

#window
window = Tk()
window.geometry("300x300")
window.title("Password Generator")

#lengthlabel
length = IntVar()
lengthlabel = Label(window, text="Password Length: ")
lengthlabel.config(anchor=CENTER)
lengthlabel.pack()
lengthinput = Entry(window, textvariable=length)
lengthinput.pack()

#amountlabel
amount = IntVar()
amountlabel = Label(window,text = "Amount of Passwords")
amountlabel.config(anchor=CENTER)
amountlabel.pack()
amountinput = Entry(window, textvariable=amount)
amountinput.pack()

#logcheckbox
checkboxinput = IntVar()
checkbox = Checkbutton(window, text="Do you want to log this password?", variable = checkboxinput, onvalue=1, offvalue=0)
checkbox.pack()

#adding a call function on click
def showMsg():
    text_file = open("password.txt", "r")
    passwordlist = []
    for line in text_file.readlines():
        if line != "\n":
            line = line.strip()
            passwordlist.append(line)
    text_file.close()
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    for i in range(amount.get()):
        password = ""
        for j in range(length.get()):
            password = password + random.choice(characters)
        if checkboxinput.get() == 1:
            passwordlist.append(password)
    boxstring = 'Your passwords have been generated!\n'
    for i in range(len(passwordlist)):
        boxstring = boxstring + passwordlist[i-1]+"\n"
    messagebox.showinfo('Password', boxstring)
    if len(passwordlist)!= 0:
        updated_file = open("password.txt", "w")
        for line in passwordlist:
            line = line.strip()
            updated_file.write(line+"\n")
    else:
        updated_file = open("password.txt", "r")
    updated_file.close()

#create button
button = Button(window,
                text='Submit',
                width=10,
                height=1,
                command = showMsg)
button.pack()



#felt quirky

window.mainloop()
