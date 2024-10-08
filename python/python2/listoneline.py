fruits=["apple","banana","mango","watermelon","pineapple"]
print(fruits)

newlist=[x for x in fruits if "o" in x]
print(newlist)

newlist=[x if  x!="mango" else "cherry" for x in fruits]
print(newlist)

for i in fruits:
    print(i)
    
print(len(fruits))
    
i=0
while i<len(fruits):
      print(i,fruits[i])
      i=i+1