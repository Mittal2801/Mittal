list=["ankit","amit","anita","amruta"]
count=0

for i in list:
    for j in i:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            count+=1
            
print("list=",list)
print("Total vowels=",count)
    
    
    