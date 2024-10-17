num=int(input("Enter any number:"))


if num>65 and num<90:
    print(chr(num))
    print("Upper case")
    
elif num>97 and num<122:
    print(chr(num))
    print("Lower case")
    
elif num>48 and num<57:
    print(chr(num))
    print("Special character")
    
else:
    print("Invalid number")