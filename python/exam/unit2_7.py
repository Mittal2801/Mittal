list1 = [1,1,2,2,3,3,3,3,4,4,5,5,7,8,9,7,4]
list2 = []


for i in list1:
    if i not in list2:
        list2.append(i)
        
print(list2)
    