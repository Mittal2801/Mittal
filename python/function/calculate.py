def add():
        a=int(input("enter a="))
        b=int(input("enter b="))
        ans=a+b
        print("addition=",ans)
    
def sub():
        a=int(input("enter a="))
        b=int(input("enter b="))
        ans=a-b
        print("subtraction=",ans)
    
def mul():
        a=int(input("enter a="))
        b=int(input("enter b="))
        ans=a*b
        print("multiplication=",ans)
        
def div():
        a=int(input("enter a="))
        b=int(input("enter b="))
        ans=a/b
        print("division=",ans)
        
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")

choice=int(input("enter 1 or 2 or 3 or 4"))
print("your choice is ",choice)

if choice==1:
    add()
    
elif choice==2:
    sub()
    
elif choice==3:
    mul()
    
elif choice==4:
    div()


    
print