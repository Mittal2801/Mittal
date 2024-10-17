num=int(input("enter number "))
ans=1


for i in range(1,num+1):
    ans=ans*i
    print(i,"*",end = " ")
    
print("=",ans)