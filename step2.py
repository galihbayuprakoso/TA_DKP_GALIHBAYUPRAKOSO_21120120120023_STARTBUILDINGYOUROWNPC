from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

class step2(object):
    def runstep2(self):
        #creating label
        lbwlcm = Label (text = "Start Building your own PC", font = "Helvetica 16 bold italic", fg ="grey", bg="cyan").place(x = 315, y = 10)
        lbnama = Label(text = "Nama\t:", fg ="grey", bg="cyan").place(x = 30,y = 50)
        ibudget = Label (text = "Budget\t:", fg ="grey", bg="cyan").place(x = 450, y = 50)
        lbspec = Label (text = "Spesifikasi PC", font = "Helvetica 14 bold italic", fg="blue", bg="cyan").place(x = 380, y = 85)
        lbmthr = Label(text = "Motherboard\t:", bg="cyan").place(x=30, y=120)
        lbcpu = Label(text = "CPU\t\t:", bg="cyan").place(x=450, y=120)
        lbgpu = Label(text = "GPU\t\t:", bg="cyan").place(x=30, y=150)
        lbram = Label(text = "RAM\t\t:", bg="cyan").place(x=450, y=150)
        lbpsu = Label(text = "PSU\t\t:", bg="cyan").place(x=30, y=180)
        lbcase = Label(text = "Case\t\t:", bg="cyan").place(x=450, y=180)
