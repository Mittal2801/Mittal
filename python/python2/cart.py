dict={}

user=int(input("How many item you want to buy?:"))
repeat=1
count=0


while repeat==1:
    for i in range(user):
        name=input("\t\t\t\tEnter item name:")
        price=int(input("\t\t\t\tEnter item price:"))
        dict[name]=price
        print(dict)
        count=count+price
        print("current bill is ",count)

    repeat=int(input("You again repeat this?press 1:"))
    

print("Final bill is ",count)
print("\t\t\t\t*****THANK YOU*****")



new=list(dict)
print(new)