import sys
class bank(object):
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("Noo")
        else:
            self.balance -= amount
            return self.balance
        
name = input("Enter name ")
b = bank(name)
while(True):
    print('d-deposite','w-withdraw','e-exit')
    choice=input("enter the choice ")
    if choice == 'e':
        sys.exit()
    amount = int(input("Enter amount:"))
    if choice == 'd':
        print("balance after deposite ",b.deposite(amount))
    elif choice == 'w':
        print("balance after withdraw ",b.withdraw(amount))