no=int(input("enter number:"))
ans=0

while no>0:
    r=no%10
    ans=ans+r
    no=no//10
    
    
print(ans)