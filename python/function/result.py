def total():
    total=java+php+python+html+dbms
    avg=total/5
    
    return total
    
def result(avg):
    if avg>90:
        print("Grade :A+")
    
    elif avg>80:
        print("Grade :A")
        
    elif avg>70:
        print("Grade :B+")
        
    elif avg>60:
        print("Grade :B") 
    
    elif avg>50:
        print("Grade :C")
       
    else:
       print("Fail")
       
    return avg
      
java=int(input("enter java marks="))
php=int(input("enter php marks="))
python=int(input("enter python marks="))
html=int(input("enter html marks="))
dbms=int(input("enter dbms marks="))

ans1=total()
print("total=",ans1)

x=ans1/5
ans2=result(x)
print("average=",ans2)


