def add(x,y):
        ans=a+b
        print("addition=",ans)
    
def sub(x,y):
        ans=x-y
        return ans
        #print("subtraction=",ans)
    
def mul(x,y):
        ans=a*b
        print("multiplication=",ans)
        
def div(x,y):
        ans=a/b
        print("division=",ans)
        
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")

choice=int(input("enter 1 or 2 or 3 or 4"))
print("your choice is ",choice)

a=int(input("enter a="))
b=int(input("enter b="))

if choice==1:
    add(a,b)
    
elif choice==2:
    x = sub(a,b)
    print(x)    
        
elif choice==3:
    mul(a,b)
    
elif choice==4:
    div(a,b)


    
