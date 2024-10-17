num=int(input("enter number:"))
prime=1

for i in range(2,num):
    if num%i==0:
        prime=0
        break


if prime==1:
    print("prime number")
else:
    print("not prime number")