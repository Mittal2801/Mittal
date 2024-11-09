try:
    a = eval(input("a="))
    b = eval(input("b=")) 
    ans = a/b
    
except (TypeError,SyntaxError):
    print("Error")
    
else:
    print(ans)