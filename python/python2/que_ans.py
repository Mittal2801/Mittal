question=["1. Enter your answer for name:",
          "2. Enter your answer for age:",
          "3. Enter your answer for city:",
          "4. Enter your answer for birth date:",
          "5. Enter your answer for roll no:",]

ans=['Mittal',19,'ahmedabad','28 jan',3107]


count=0
name=input("1. Enter your answer for name=")
print("Your answer :",name)
if name in ans:
    print("Pass")
    count+=1
else:
    print("Fail")
    
age=int(input("2. Enter your answer for age="))
print("Your answer :",age)
if age in ans:
    print("Pass")
    count+=1

else:
    print("Fail")
    
city=input("3. Enter your answer for city=")
print("Your answer:",city)
if city in ans:
    print("Pass")
    count+=1

else:
    print("Fail")
    
birthdate=input("4. Enter your answer for birth date=")
print("Your answer: ",birthdate)
if birthdate in ans:
    print("Pass")
    count+=1

else:
    print("Fail")
    
rollno=int(input("5. Enter your answer for roll no="))
print("Your answer=",rollno)
if rollno in ans:
    print("Pass")
    count+=1

else:
    print("Fail")
    
print("Your marks is ",count)
print("*****THANK YOU*****")