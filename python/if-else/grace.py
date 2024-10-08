marks=int(input("enter your marks :"))
print("Marks=",marks)

if marks>35:
    print("Pass")
    
else:
    if marks>32:
        sub=35-marks
        print("gracing marks ",sub)
        
    else :
        print("Fail")