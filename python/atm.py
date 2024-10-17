balance=10000
bank=1
wcount=0
dcount=0
count=0
wtotal=0
dtotal=0
opBal=balance


while bank==1:
    print("your opening balance is ",balance)
    choice=int(input("press 1 for withdraw \n press 2 for deposite \n press 3 for check current balance"))
    if choice==1:
        wamt=int(input("enter withdraw amount:"))
        if wamt>balance:
                        print("Insufficiant balance")
        else:
            balance-=wamt
            wcount+=1
            print("Your current balance is  ",balance)
            camount=print("your amount ",wamt)
            wtotal+=wamt
       
    elif choice==2:
        damt=int(input("enter deposite amount:"))
        balance+=damt
        dcount+=1
        print("your current balance is ",balance)
        camount=print("your amount ",damt)
        dtotal+=damt
        
            
    elif choice==3:
        
        print("your balance is=",balance)
        count+=1
        
    else:
        print("you choice wrong number")
        
    
    
print("withdraw ",wcount,"time")
print("deposite ",dcount,"time")
print("check ",count,"time")
    
bank=int(input("Do you want to check again yes for 1 no for other"))


print("Opening balance=",opBal)
print("total withdraw amount=",wtotal)
print("total deposite amount=",dtotal)
print("closing balance=",balance)