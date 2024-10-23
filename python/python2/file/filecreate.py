f1 = open("first.txt","w")
f1.write("Hello")
f1.write("\nMy name is Mittal")
print("file created")

f1 = open("first.txt","r")
print(f1.read())