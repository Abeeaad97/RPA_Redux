# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:55:20 2021

@author: Abid B
"""
import baseFile
def run_button():
    UN = userName.get()
    PW = passWord.get()
    baseFile.main(UN, PW)
    print("Program ran")
import tkinter as tk 
window = tk.Tk()

window.title("Alter Odces RPA")
lbl = tk.Label(window, text="Please enter your ODCES Log in and click the run button", font = ("Arial Bold", 18))
userLBL = tk.Label(window, text="User Name or Email").grid(row = 4)
passLBL = tk.Label(window, text="Password").grid(row = 9)

userName = tk.Entry(window)
passWord = tk.Entry(window, show = "*")
run = tk.Button(window, text = "Run", command = lambda:run_button())


#Grid setup 
lbl.grid(column=0, row=0)
userName.grid(column = 0, row = 5)
passWord.grid(column = 0, row = 10)
run.grid(column = 0, row = 15)




window.mainloop()

'''
Thank you for reaching out to the BeWell Line, you are not alone. While you wait to be connected with one of our counselors, please share what brought you here today. 

If at any moment you need the conversation to end, please reply STOP and the chat will close immediately. 

One conversation may not solve everything, but it's the first step in the right direction. Getting back to feeling more like yourself. We are here 24/7, if you ever feel yourself in a crisis again, please reach out to us. You are not alone.
201 Characters, breaks the message. 

Ask Veronica about sending a link to SMS to require terms and conditions agreement  
'''