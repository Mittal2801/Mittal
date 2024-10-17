def reverce():
    no=int(input("enter no:"))
    ans=0
    while no>0:
        r=no%10
        ans=ans*10+r
        no=no//10
        
    print(ans)
    
def prime():
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
            
def armstrong():
    no=int(input("enter no:"))
    ans=0
    new=no
    
    while no>0:
        r=no%10
        print(r)
        ans=ans+r**3
        print(ans)
        no=no//10
    
    if new==ans:
        print("armstrong number")
    else:
        print("not armstrong number")
        
def factorial(no):
    ans=1
    
    
    while no>=1:
        ans=ans*no
        print(no,"*",end = " ")
        no-=1
                
    return ans
    
def fibonacii():
    n1=0
    n2=1
    
    no=int(input("enter number:"))
    i=2
    print(n1,n2,end=" ")
    
    while i<no:
        temp=n1+n2
        print(temp,end=" ")
        n1=n2
        n2=temp
        i=i+1
                         
print("press 1 for reverce")
print("press 2 for prime number")
print("press 3 for armstrong number")
print("press 4 for factorial")
print("press 5 for fibonacci")

choice=int(input("enter any number:"))
print("your choice is ",choice)

if choice==1:
    reverce()
    
elif choice==2:
    prime()
    
elif choice==3:
    armstrong()
    
elif choice==4:
    x=int(input("enter number:"))
    total=factorial(x)

    print("=",total)  
      
elif choice==5:
    fibonacii()
    
    
    
    