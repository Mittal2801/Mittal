def factorial(no):
    ans=1
    for i in range(1,no+1):
        ans=ans*i
        print(i,"*",end=" ")
    
    return ans
    
def fibonacii(f1):
    n1=0
    n2=1
    for i in range(2,f1):
        temp=n1+n2
        print(temp,end=" ")
        n1=n2
        n2=temp
        
# num=int(input("enter number:"))

# factorial(num)

# fibonacii(num)