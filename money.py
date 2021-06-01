#money format (setter getter)
class money(object):
    __money1 = 0
    __money2 = 0
    __money3 = 0
    __money4 = 0

    def __init__(self, totalprice, lack, orbdgt, restof):
        self.__money1 = totalprice
        self.__money2 = lack
        self.__money3 = orbdgt
        self.__money4 = restof

    #setter
    def setmoney1(self, totalprice):
        self.__money1 = totalprice
        pass
            
    def setmoney2(self, lack):
        self.__money2 = lack
        pass
    
    def setmoney3(self, orbdgt):
        self.__money3 = orbdgt
        pass

    def setmoney4(self, restof):
        self.__money4 = restof
        pass

    #getter
    def getmoney1(self):
        ttl = str(self.__money1)
        t  = 0
        out = ''
        for i in (ttl[::-1]):
            if t == 3:
                out += '.'+i
                t=1
            else:
                out += i
                t += 1
        total = out[::-1]
        return total

    def getmoney2(self):
        lck = str(self.__money2)
        t  = 0
        out = ''
        for i in (lck[::-1]):
            if t == 3:
                out += '.'+i
                t=1
            else:
                out += i
                t += 1
        lom = out[::-1]
        return lom
            
    def getmoney3(self):
        rbdgt = str(self.__money3)
        t  = 0
        out = ''
        for i in (rbdgt[::-1]):
            if t == 3:
                out += '.'+i
                t=1
            else:
                out += i
                t += 1
        rbdgt = out[::-1]
        return rbdgt
            
    def getmoney4(self):
        restofmoney = str(self.__money4)
        t  = 0
        out = ''
        for i in (restofmoney[::-1]):
            if t == 3:
                out += '.'+i
                t=1
            else:
                out += i
                t += 1
        restmny = out[::-1]
        return restmny
