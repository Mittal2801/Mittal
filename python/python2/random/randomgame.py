import random
amount=100




while amount >30:
    num=int(input("Enter any number 1 to 10:"))
    r=random.randrange(1,10)
    print(r)
    

    if num==r:
        amount+=50
        print("balance is=",amount)
        
    else:
        amount-=30
        print("balance is=",amount)
        

        




