price=float(input("enter price"))
print("price=",price)

qty=int(input("enter qty"))
print("qty=",qty)

ans=price*qty

if ans>10000:
    p1=ans*25/100
    print("25% discount",p1)
    
    
else:
    p2=ans*15/100
    print("15% discount",p2)
    