num=int(input("enter number="))
ans=0
new=num

while num>0:
    r=num%10
    print(r)
    ans=ans+r**3
    print(ans)
    num=num//10
print(ans)

if new==ans:
    print("armstrong number")
else:
    print("not armstrong number")

