from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from step1 import step1
from step2 import step2
from step3 import step3
from money import money
from step4 import step4


top = Tk()  
top.geometry("900x600")
top.resizable(False,False)
top.configure(bg="cyan")
top.title("Start building your own PC")


#creating label
lbwlcm = Label (text = "Start Building your own PC", font = "Helvetica 16 bold italic", fg ="blue", bg="cyan").place(x = 315, y = 10)
lbnama = Label(text = "Nama\t:", bg="cyan").place(x = 30,y = 50)
ibudget = Label (text = "Budget\t:", bg="cyan").place(x = 450, y = 50)
#lbjk = Label(text = "Gender\t:").place(x = 30, y=40)

#create input  
nama = StringVar()
inama = Entry(top,width = 45, textvariable=nama).place(x = 110, y = 50)
budget = StringVar()
ibudget = Entry(width = 45, textvariable=budget).place(x = 530, y = 50)


def runstep1():
    nama1 = nama.get()
    budget1 = budget.get()
                
    openstep1 = step1(nama1, budget1)
    openstep1.usrbudget()
    return

#create button
btn1 = Button(command = runstep1, text="SUBMIT").place(x=820,y=47)


top.mainloop()    
