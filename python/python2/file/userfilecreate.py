name = input("Enter your file name:")

f1 = open(name+".txt","w")

for i in range(5):
    user = input("Enter name:")
    f1.write(user)
    f1.write("\n")
    
f1 = open(name+".txt","r")
print(f1.read())
