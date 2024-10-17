def fact(x):
    ans=1

    for i in range(1,x+1):
        ans=ans*i
        print(x,"*",end=" ")
        
        
    print(ans)
    
num=int(input("enter any number="))
fact(num)

