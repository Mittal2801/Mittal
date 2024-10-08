num=int(input("enter number:"))
ans=0
new=num

while num>0:
    r=num%10
    ans=ans*10+r
    num=num//10
    
print(ans)

if new==ans:
    print("perfect number")
else:
    print("not perfect number")