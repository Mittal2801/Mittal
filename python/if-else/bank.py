bal=int(input("Enter your opening balance :"))
print("Your Opening balance :",bal)


print("enter 1 for deposite")
print("enter 2 for withdraw")

choice=int(input("enter 1 or 2 :"))
print("your choice is ",choice)

if choice==1:
    damt=int(input("please enter deposite amount :"))
    deposite=bal+damt
    print("current balance=",deposite)
    
else:
    wamt=int(input("please enter withdraw amount :"))
    if bal >=wamt:
        withdraw=bal-wamt
        print("current balance=",withdraw) 
    else :
        print("Insufficient balance")                                                