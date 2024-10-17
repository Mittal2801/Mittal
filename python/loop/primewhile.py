no=int(input("enter no:"))
i=2
prime=0
     
while i<=no/2:
    if no%i==0:
        prime=1
        break
    i=i+1
       
            
if prime==0:
        print("prime number")
                
                
else:
        print("not prime number")
            