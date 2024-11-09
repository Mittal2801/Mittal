a = int(input("a="))
b = int(input("b="))

try:
    ans = a/b
except ZeroDivisionError:
    print("zero")
    
else:
    print(ans)