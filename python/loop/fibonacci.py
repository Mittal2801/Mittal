# n1=0
# n2=1

# user=int(input("enter number:"))
# i=2
# print(n1," ",n2 ," ",end = "")

# while i<user:
#     temp = n1+n2
#     print(temp,end=" ")
#     n1=n2
#     n2=temp
#     i+=1

n1=0
n2=1

num=int(input("enter num="))
i=2
print(n1,n2,end=" ")

while i<num:
    temp=n1+n2
    print(temp,end = " ")
    n1=n2
    n2=temp
    i=i+1