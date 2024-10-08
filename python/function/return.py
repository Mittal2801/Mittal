def add(one,two):
    ans=one+two
    return ans

def mul(first,second):
    ans=first*second
    return ans

x=int(input("enter x:"))
y=int(input("enter y:"))

total=add(x,y)
print("total=",total)

z=int(input("enter value for multiplication:"))

mul=mul(total,z)
print("multiplication=",mul)