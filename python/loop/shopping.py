total=0
count=0

while total<10000:
    amt=int(input("enter amount:"))
    total=total+amt
    print("your amount is ",amt,"remaining amount is ",10000-total)
    count+=1
    
print("thank you for shopping",count,"items")