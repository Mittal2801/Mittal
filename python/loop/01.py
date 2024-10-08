row = int(input("enter no of row "))
col = int(input("enter no of column "))
                                
count = 1
for i in range(row):
    for j in range(col):
        print(count%2 , end = " ")
        count += 1 
    print("\n")