def one():
    for i in range(0,5):
        for j in range(0,5):
            print("*",end=" ")
        print(" ")
        
def two():
    for i in range(0,5):
        for j in range(i):
            print("*",end=" ")
        print(" ")
        
def three():
    for i in range(0,5):
        for k in range(5-i):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print(" ")
        
def four():
    for i in range(5,0,-1):
        for k  in range(5-i):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print(" ")
        
def five():
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end=" ")
        print(" ")
        
def corn():
    for i in range(5,0,-1):
        for k in range(5-i):
            print(" ",end="")
        for j in range(i):
            print("*",end=" ")
        print(" ")
    
def hill():
    for i in range(0,6):
        for k in range(5-i):
            print(" ",end="")
        for j in range(i):
            print("*",end=" ")
        print(" ")
        
def eight():
    for i in range(0,5):
        for j in range(0,5):
            print(i,end=" ")
        print(" ")
        
def nine():
    for i in range(0,5):
        for j in range(0,5):
            print(j,end=" ")
        print(" ")
        
def ten():
    count=65
    for i in range(0,5):
        for j in range(0,5):
            print(chr(count),end=" ")
            count+=1
        print(" ")   
        
print("press 1 for 5star")
print("press 2 for leftpattern")
print("press 3 for right pattern")
print("press 4 for right pattern reverce")
print("press 5 for left pattern reverce")
print("press 6 for corn")
print("press 7 four hill")
print("press 8 for 00000")
print("press 9 for 01234")
print("press 10 for ABCDE")

choice=int(input("enter any number:"))
print("your choice is ",choice)

if choice==1:
    one()
    
elif choice==2:
    two()
    
elif choice==3:
    three()
    
elif choice==4:
    four()
    
elif choice==5:
    five()
    
elif choice==6:
    corn()
    
elif choice==7:
    hill()
    
elif choice==8:
    eight()
    
elif choice==9:
    nine()
    
elif choice==10:
    ten()