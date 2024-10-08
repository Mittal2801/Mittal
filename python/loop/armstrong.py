no=int(input("enter no="))
ans=0
new=no

while no>0:
    r=no%10
    print(r)
    ans+=r**3
    print(ans)
    no=no//10
    
    
print(ans)


if new==ans:
    print("armstrong")
else:
    print("not armstrong")






