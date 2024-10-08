first=int(input("Enter first value :"))
second=int(input("Enter second value :"))
third=int(input("Enter third value :"))

if first>second and first>third:
    print("first is max")
    
elif second>first and second>third:
    print("second is max")
    
else:
    print("third is max")