class Bank(object):
    cash = 1000000
    @classmethod
    def Cashes(cls):
        print(cls.Cashes)
class Andhrabank(Bank):
    pass
class Statebank(Bank):
    cash = 200000
    @classmethod
    def Chases(cls):
        print(cls.cash+Bank.cash)
    
a = Andhrabank()
a.Cashes()
s = Statebank()
s.Chases()