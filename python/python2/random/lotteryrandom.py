import random

list=random.sample(range(1,75),6)
print("List=",list)

user=int(input("Enter any number:-"))
print("User choice=",user)

com=random.choice(list)
print("Computer choice=",com)

# user=int(input("Enter any number:-"))
# print("User choice=",user)

if com==user:
    print("You won lottery")
    
else:
    print("Next time")