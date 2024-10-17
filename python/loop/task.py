no=75645236
ans=0
count=0


while no>0:
        r=no%10
        
        if r%2==0: 
            ans=ans+r
            print(ans)
            count+=1
    
        no=no//10
        
print(ans)
print(count)