row = int(input("enter no of row "))
col = int(input("enter no of column "))

# for i in range(row):
#     for j in range(col):
#         print(i , end = " ")
#     print("\n")


count = 97
for i in range(row):
    for j in range(col):
        print(chr(count) , end = " ")
        count += 1 
    print("\n")