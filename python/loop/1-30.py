col=int(input("enter col="))
row=int(input("enter row="))


count = 1
for i in range(row):
    for j in range(col):
        print(count , end = " ")
        count += 1 
    print("\n")