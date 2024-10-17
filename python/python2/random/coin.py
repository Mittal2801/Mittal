import random

coin=['h','t']
counth=0
countt=0

for i in range(1,100):
    ans=random.choice(coin)
    
    if ans=='h':
        counth+=1
    
    else:
        countt+=1
        
        
print("h:",counth)
print("t:",countt)