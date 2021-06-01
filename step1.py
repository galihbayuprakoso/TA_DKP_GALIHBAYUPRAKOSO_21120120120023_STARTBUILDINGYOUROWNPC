from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from step2 import step2
from step3 import step3
from money import money
from step4 import step4

class step1(object):
    def __init__(self, nama1, budget1):
        self.nama1 = nama1
        self.budget1 = budget1
        
    def usrbudget(self):
        if len(self.nama1) == 0:
            messagebox.showerror("NAMA","BELUM MENGISI NAMA")
            return
        if len(self.budget1) == 0:
            messagebox.showerror("BUDGET","BELUM MENGISI BUDGET")
            return
        try:
            int(self.budget1)
            lbbdgterror = Label (text = "*Masukkan nominal angka", fg="cyan", bg="cyan").place(x = 525, y = 70)
        except ValueError:
            messagebox.showerror("BUDGET","MASUKKAN NOMINAL ANGKA")
            lbbdgterror = Label (text = "*Masukkan nominal angka", fg="red", bg="cyan").place(x = 525, y = 70)
            return
        #if radio.get()== 0:
            #messagebox.showerror("Error","BELUM MEMILIH JENIS KELAMIN")
            #return
        #elif radio.get() == 1:
            #perkenalan="Mas "
        #elif radio.get() == 2:
            #perkenalan="Mbak "

            
        #button state
        btn1 = Button(command = step1, text="SUBMIT", state="disable").place(x=820,y=47)

        #input state
        inama = Entry(width = 45, textvariable=self.nama1, state="disable").place(x = 110, y = 50)
        lbnama = Label (width=39, text = self.nama1, anchor="w", fg="grey").place(x = 110, y = 50)
        ibudget = Entry(width = 45, textvariable=self.budget1, state="disable").place(x = 530, y = 50)
        lbbudget = Label (width=39, text = self.budget1, anchor="w", fg="grey").place(x = 530, y = 50)
        
        #step2 label
        openstep2 = step2()
        openstep2.runstep2()
        
        #create combobox
        strmthr = StringVar(value='-pilih-') 
        Mthr = ttk.Combobox( width = 35, textvariable = strmthr, state="readonly")
        Mthr.place(x=150, y=120)
        
        strcpu = StringVar(value='-pilih-') 
        Cpu = ttk.Combobox(width = 35, textvariable = strcpu, state="readonly")
        Cpu.place(x=570, y=120)

        strgpu = StringVar(value='-pilih-') 
        Gpu = ttk.Combobox(width = 35, textvariable = strgpu, state="readonly")
        Gpu.place(x=150, y=150)

        strram = StringVar(value='-pilih-') 
        RAM = ttk.Combobox( width = 35, textvariable = strram, state="readonly")
        RAM.place(x=570, y=150)

        strpsu = StringVar(value='-pilih-') 
        psu = ttk.Combobox(width = 35, textvariable = strpsu, state="readonly")
        psu.place(x=150, y=180)
        
        strcase = StringVar(value='-pilih-') 
        case = ttk.Combobox( width = 35, textvariable = strcase, state="readonly")
        case.place(x=570, y=180)

        # Adding combobox drop down list 
        Mthr['values'] = ('ASUS ROG - 2.500.000', 'ASUS TUF - 2.200.000','MSI Tomahawk - 2.000.000', 'GIGABYTE AORUS - 3.500.000','Biostar Valkryie - 6.750.000') 
        Cpu['values'] = ('Intel Core i3 - 2.000.000', 'Intel Core i5 - 3.000.000', 'Intel Core i7 - 5.000.000', 'Intel Core i9 - 7.000.000', 'AMD Ryzen 7 - 7.300.000')
        Gpu['values'] = ('ASUS TUF RTX 3060 - 14.000.000', 'ASUS strix RTX 3070 - 34.000.000', 'Nvidia RTX 3080 - 38.500.000', 'MSI RTX 3090 - 45.000.000', 'Radeon RX 6900 XT - 28.000.000')
        RAM['values'] = ('8 GB - 800.000', '16 GB - 1.600.000', '32 GB - 3.200.000', '64 GB - 6.400.000', '128 GB - 20.000.000')
        psu['values'] = ('Corsair 750W Gold - 2.000.000', 'DA 800W Gold - 1.100.000', 'ASUS ROG Strix 850W Gold - 3.750.000' , 'Corsair 1000 W Gold - 6.000.000', 'EVGA 1300W Gold - 8.000.000')
        case['values'] = ('Corsair Icue 465 - 2.200.000', 'Lian Li 011 XL - 3.600.000', 'NZXT H510 - 1.300.000', 'Corsair 4000D - 1.400.000', 'Thermaltake A500 - 5.000.000')

        #budget (integer)
        bdgt = int(self.budget1)

        def spec():
            #step3 input declaration
            motherboard =  strmthr.get()
            processor = strcpu.get()
            graphic = strgpu.get()
            randommem = strram.get()
            powersupp = strpsu.get()
            casing = strcase.get()

            #step3 
            openstep3 = step3(motherboard, processor, graphic, randommem, powersupp, casing)
            pricemthr, namemthr = openstep3.get_motherboard()
            pricecpu, namecpu = openstep3.get_processor()
            pricegpu, namegpu = openstep3.get_graphic()
            priceram, nameram = openstep3.get_randommem()
            pricepsu, namepsu = openstep3.get_powersupp()
            pricecase, namecase = openstep3.get_casing()
            
            #combobox state
            Mthr = ttk.Combobox( width = 35, textvariable = strmthr, state="disable")
            Mthr.place(x=150, y=120)
            
            Cpu = ttk.Combobox(width = 35, textvariable = strcpu, state="disable")
            Cpu.place(x=570, y=120)
            
            Gpu = ttk.Combobox(width = 35, textvariable = strgpu, state="disable")
            Gpu.place(x=150, y=150)
            
            RAM = ttk.Combobox( width = 35, textvariable = strram, state="disable")
            RAM.place(x=570, y=150)
            
            psu = ttk.Combobox(width = 35, textvariable = strpsu, state="disable")
            psu.place(x=150, y=180)
            
            case = ttk.Combobox( width = 35, textvariable = strcase, state="disable")
            case.place(x=570, y=180)


            #money calculations (total)
            totalprice = pricemthr+pricecpu+pricegpu+priceram+pricepsu+pricecase
            
            #money calculations (lack)
            lack = bdgt-totalprice
            lack = lack*(-1)

            #money calculations (original budget)
            orbdgt = bdgt
            
            #money calculations (rest om money)
            restof = bdgt-totalprice

            #money format
            mon = money(totalprice, lack, orbdgt, restof)
            
            #creating label
            lbspec = Label (text = "Spesifikasi PC", font = "Helvetica 14 bold italic", fg="grey", bg="cyan").place(x = 380, y = 85)
            lbmthr = Label(text = "Motherboard\t:", fg="grey", bg="cyan").place(x=30, y=120)
            lbcpu = Label(text = "CPU\t\t:", fg="grey", bg="cyan").place(x=450, y=120)
            lbgpu = Label(text = "GPU\t\t:", fg="grey", bg="cyan").place(x=30, y=150)
            lbram = Label(text = "RAM\t\t:", fg="grey", bg="cyan").place(x=450, y=150)
            lbpsu = Label(text = "PSU\t\t:", fg="grey", bg="cyan").place(x=30, y=180)
            lbcase = Label(text = "Case\t\t:", fg="grey", bg="cyan").place(x=450, y=180)
            

            #step4 customer
            lbbill = Label (text = "Builder", font = "font 10 bold italic ",  bg="cyan").place(x = 30, y = 220)
            lbcsname = Label (text = "Nama \t\t: " + str(self.nama1), bg="cyan").place(x=30, y=250)
            lbcsbudget = Label (text = "Budget \t\t: Rp. " + str(mon.getmoney3()) + ",-", bg="cyan").place(x=30, y=270)


            #output color
            color = step4(totalprice, bdgt)


                #lbover = Label(text = "Budget tidak mencukupi (- Rp. " + str(mon.getmoney2()) + ",-)", fg =clr, bg="cyan").place(x=30, y=430)
                #return
            #step4 spec
            lbspec = Label (text = "Spesifikasi PC", font = "font 10 bold italic ",  bg="cyan").place(x=30, y=300)
            lbusrmthr = Label(text = "Motherboard\t: " + namemthr, fg=color.getclr(), bg="cyan" ).place(x=30, y=330)
            lbusrcpu = Label(text = "CPU\t\t: " + namecpu, fg=color.getclr(), bg="cyan" ).place(x=30, y=350)
            lbusrgpu = Label(text = "GPU\t\t: " + namegpu, fg=color.getclr(), bg="cyan" ).place(x=30, y=370)
            lbusrram = Label(text = "RAM\t\t: " + nameram, fg=color.getclr(), bg="cyan" ).place(x=30, y=390)
            lbusrpsu = Label(text = "PSU\t\t: " + namepsu, fg=color.getclr(), bg="cyan").place(x=30, y=410)
            lbusrcase = Label(text = "Case\t\t: " + namecase, fg=color.getclr(), bg="cyan").place(x=30, y=430)

            #step4 price
            lbhdrtotal = Label (text = "Total Harga PC",  font = "font 10 bold italic ",  bg="cyan").place(x=30, y=460)
            lbtotal = Label (text = "Total harga PC \t: Rp. " + str(mon.getmoney1()) + ",-",fg=color.getclr(), bg="cyan").place(x=30, y=490)
            color.lackofmoney()
            color.amountofmoney()
            
            #pesan = "Halo " + strmthr.get() + strcpu.get() + strgpu.get() + strram.get() + strpsu.get()+ strcase.get() +budget.get() + "!!!"
            #messagebox.showinfo("Greeting", pesan)
            
            #button state
            btn2 = Button(command = spec, text="SUBMIT", state="disable").place(x=820,y=178)

            
        #create button
        btn2 = Button(command = spec, text="SUBMIT").place(x=820,y=178)
