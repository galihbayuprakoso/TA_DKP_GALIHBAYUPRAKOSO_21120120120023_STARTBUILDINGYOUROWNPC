from tkinter import * 
from tkinter import ttk

#setp4 color
class step4(object):
    totalprice = 0
    bdgt = 0
    def __init__(self,totalprice, bdgt):
        self.totalprice = totalprice
        self.bdgt = bdgt

    def getclr(self):
        if self.totalprice<self.bdgt:
            clr = "black"
        else:
            clr = "red"
        return clr
    
    def lackofmoney(self):
        if self.totalprice<self.bdgt:
            total = self.bdgt-self.totalprice
            lomtotal = str(total)
            t  = 0
            out = ''
            for i in (lomtotal[::-1]):
                if t == 3:
                    out += '.'+i
                    t=1
                else:
                    out += i
                    t += 1
            lomtotal = out[::-1]
            lbrest = Label (text = "Sisa budget anda\t: Rp, " + lomtotal + ",-", bg="cyan").place(x=30, y=510)
        else:
            total = self.bdgt-self.totalprice
            lomtotal = str(total)
            t  = 0
            out = ''
            for i in (lomtotal[::-1]):
                if t == 3:
                    out += '.'+i
                    t=1
                else:
                    out += i
                    t += 1
            lomtotal = out[::-1]
            lbrest = Label (text = "Budget kurang\t: Rp, " + lomtotal + ",-", fg = "red", bg="cyan").place(x=30, y=510)
        return lbrest
    def amountofmoney(self):
        if self.totalprice<self.bdgt:
            lbthanks = Label (text = "Anda bisa merakit PC Anda sekarang", font = "Helvetica 16 bold italic", fg ="blue", bg="cyan").place(x = 255, y = 540)
        else:
            lbthanks = Label (text = "Maaf Budget Anda tidak mencukupi", font = "Helvetica 16 bold italic", fg ="red", bg="cyan").place(x = 270, y = 540)
        return lbthanks
        
