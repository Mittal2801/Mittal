java=int(input("enter java marks :"))

python=int(input("enter python marks :"))

php=int(input("enter php marks :"))

html=int(input("enter html marks :"))

dbms=int(input("enter dbms marks :"))




total=java+python+php+html+dbms
print("Total=",total)

avg=total/5
print("Avg=",avg)

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
    