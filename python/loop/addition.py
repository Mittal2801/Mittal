count=0
ans=0

for i in range(1,11):
    user=int(input("enter product value:"))
    
    if user>300 and user<500:
        ans=ans+user      
        count+=1
  
print("total=",ans)        
print("total products=",count)