def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num%i) ==0:
                print(num,"is not prime num")
                break
            else:
                print(num,"is prime number")
                break
                
    else:
        print("not prime num")
                
                
                
num = int(input("enter the num = "))
prime(num)
                