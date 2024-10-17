n1=0
n2=1



num=int(input("enter number="))
print(n1," ",n2,end = " ")

for i in range(2,num):
    temp=n1+n2
    print(temp,end=" ")
    n1=n2
    n2=temp
    i=i+1

 
 
 
