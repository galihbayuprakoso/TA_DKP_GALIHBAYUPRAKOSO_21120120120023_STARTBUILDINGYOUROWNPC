from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

class step3(object):
    def __init__(self, motherboard, processor, graphic, randommem, powersupp, casing):
        self.motherboard = motherboard
        self.processor = processor
        self.graphic = graphic
        self.randommem = randommem
        self.powersupp = powersupp
        self.casing = casing
        
    def get_motherboard(self):
        #motherboard 'ASUS ROG - 2.500.000', 'ASUS TUF - 2.200.000','MSI Tomahawk - 2.000.000', 'GIGABYTE AORUS - 3.500.000','Biostar Valkryie - 6.750.000'
        pricemthr = 0
        namemthr = ' '
        if self.motherboard == '-pilih-':
            messagebox.showerror("Error","BELUM MEMILIH MOTHERBOARD")
            return
        if self.motherboard == 'ASUS ROG - 2.500.000':
            pricemthr = pricemthr+2500000
            namemthr = 'ASUS ROG'
            return pricemthr, namemthr
        if self.motherboard == 'ASUS TUF - 2.200.000':
            pricemthr = pricemthr+2200000
            namemthr = 'ASUS TUF'
            return pricemthr, namemthr
        if self.motherboard == 'MSI Tomahawk - 2.000.000':
            pricemthr = pricemthr+2000000
            namemthr = 'MSI Tomahawk'
            return pricemthr, namemthr
        if self.motherboard == 'GIGABYTE AORUS - 3.500.000':
            pricemthr = pricemthr+3500000
            namemthr = 'GIGABYTE AORUS'
            return pricemthr, namemthr
        if self.motherboard == 'Biostar Valkryie - 6.750.000':
            pricemthr = pricemthr+6750000
            namemthr = 'Biostar Valkryie'
            return pricemthr, namemthr

    def get_processor(self):
        #CPU 'Intel Core i3 - 2.000.000', 'Intel Core i5 - 3.000.000', 'Intel Core i7 - 5.000.000', 'Intel Core i9 - 7.000.000', 'AMD Ryzen 7 - 7.300.000'
        pricecpu = 0
        namecpu = ' '
        if self.processor == '-pilih-':
            messagebox.showerror("Error","BELUM MEMILIH CPU")
            return
        if self.processor == 'Intel Core i3 - 2.000.000':
            pricecpu = pricecpu+2000000
            namecpu = 'Intel Core i3'
            return pricecpu, namecpu
        if self.processor == 'Intel Core i5 - 3.000.000':
            pricecpu = pricecpu+3000000
            namecpu = 'Intel Core i5'
            return pricecpu, namecpu
        if self.processor == 'Intel Core i7 - 5.000.000':
            pricecpu = pricecpu+5000000
            namecpu = 'Intel Core i7'
            return pricecpu, namecpu
        if self.processor == 'Intel Core i9 - 7.000.000':
            pricecpu = pricecpu+7000000
            namecpu = 'Intel Core i9'
            return pricecpu, namecpu
        if self.processor == 'AMD Ryzen 7 - 7.300.000':
            pricecpu = pricecpu+7300000
            namecpu = 'AMD Ryzen 7'
            return pricecpu, namecpu

    def get_graphic(self):
        #GPU 'ASUS TUF RTX 3060 - 14.000.000', 'ASUS strix RTX 3070 - 34.000.000', 'Nvidia RTX 3080 - 38.500.000', 'MSI RTX 3090 - 45.000.000', 'Radeon RX 6900 XT - 28.000.000'
        pricegpu = 0
        namegpu = ' '
        if self.graphic == '-pilih-':
            messagebox.showerror("Error","BELUM MEMILIH GPU")
            return
        if self.graphic == 'ASUS TUF RTX 3060 - 14.000.000':
            pricegpu = pricegpu+14000000
            namegpu = 'ASUS TUF RTX 306'
            return pricegpu, namegpu
        if self.graphic == 'ASUS strix RTX 3070 - 34.000.000':
            pricegpu = pricegpu+34000000
            namegpu = 'ASUS strix RTX 3070'
            return pricegpu, namegpu
        if self.graphic == 'Nvidia RTX 3080 - 38.500.000':
            pricegpu = pricegpu+38500000
            namegpu = 'Nvidia RTX 3080'
            return pricegpu, namegpu
        if self.graphic == 'MSI RTX 3090 - 45.000.000':
            pricegpu = pricegpu+45000000
            namegpu = 'MSI RTX 3090'
            return pricegpu, namegpu
        if self.graphic == 'Radeon RX 6900 XT - 28.000.000':
            pricegpu = pricegpu+28000000
            namegpu = 'Radeon RX 6900 XT'
            return pricegpu, namegpu

    def get_randommem(self):
        #RAM '8 GB - 800.000', '16 GB - 1.600.000', '32 GB - 3.200.000', '64 GB - 6.400.000', '128 GB - 20.000.000'
        priceram = 0
        nameram = ' '
        if self.randommem == '-pilih-':
            messagebox.showerror("Error","BELUM MEMILIH RAM")
            return
        if self.randommem == '8 GB - 800.000':
            priceram = priceram+800000
            nameram = '8 GB'
            return priceram, nameram
        if self.randommem == '16 GB - 1.600.000':
            priceram = priceram+1600000
            nameram = '16 GB'
            return priceram, nameram
        if self.randommem == '32 GB - 3.200.000':
            priceram = priceram+3200000
            nameram = '32 GB'
            return priceram, nameram
        if self.randommem == '64 GB - 6.400.000':
            priceram = priceram+6400000
            nameram = '64 GB'
            return priceram, nameram
        if self.randommem == '128 GB - 20.000.000':
            priceram = priceram+20000000
            nameram = '128 GB'
            return priceram, nameram

    def get_powersupp(self):
        #PSU 'Corsair 750W Gold - 2.000.000', 'DA 800W Gold - 1.100.000', 'ASUS ROG Strix 850W Gold - 3.750.000' , 'Corsair 1000 W Gold - 6.000.000', 'EVGA 1300W Gold - 8.000.000'
        pricepsu = 0
        namepsu = ' '
        if self.powersupp == '-pilih-':
            messagebox.showerror("Error","BELUM MEMILIH PSU")
            return
        if self.powersupp == 'Corsair 750W Gold - 2.000.000':
            pricepsu = pricepsu+2000000
            namepsu = 'Corsair 750W Gold'
            return pricepsu, namepsu
        if self.powersupp == 'DA 800W Gold - 1.100.000':
            pricepsu = pricepsu+1100000
            namepsu = 'DA 800W Gold'
            return pricepsu, namepsu
        if self.powersupp == 'ASUS ROG Strix 850W Gold - 3.750.000':
            pricepsu = pricepsu+3750000
            namepsu = 'ASUS ROG Strix 850W Gold'
            return pricepsu, namepsu
        if self.powersupp == 'Corsair 1000 W Gold - 6.000.000':
            pricepsu = pricepsu+6000000
            namepsu = 'Corsair 1000 W Gold'
            return pricepsu, namepsu
        if self.powersupp == 'EVGA 1300W Gold - 8.000.000':
            pricepsu = pricepsu+8000000
            namepsu = 'EVGA 1300W Gold'
            return pricepsu, namepsu

    def get_casing(self):
        #case 'Corsair Icue 465 - 2.200.000', 'Lian Li 011 XL - 3.600.000', 'NZXT H510 - 1.300.000', 'Corsair 4000D - 1.400.000', 'Thermaltake A500 - 5.000.000'
        pricecase = 0
        namecase = ' '
        if self.casing == '-pilih-':
            messagebox.showerror("Error","BELUM MEMILIH CASE")
            return
        if self.casing == 'Corsair Icue 465 - 2.200.000':
            pricecase = pricecase+2200000
            namecase = 'Corsair Icue 465'
            return pricecase, namecase
        if self.casing == 'Lian Li 011 XL - 3.600.000':
            pricecase = pricecase+3600000
            namecase = 'Lian Li 011 XL'
            return pricecase, namecase
        if self.casing == 'NZXT H510 - 1.300.000':
            pricecase = pricecase+1300000
            namecase = 'NZXT H510'
            return pricecase, namecase
        if self.casing == 'Corsair 4000D - 1.400.000':
            pricecase = pricecase+1400000
            namecase = 'Corsair 4000D'
            return pricecase, namecase
        if self.casing == 'Thermaltake A500 - 5.000.000':
            pricecase = pricecase+5000000
            namecase = 'Thermaltake A500'
            return pricecase, namecase


