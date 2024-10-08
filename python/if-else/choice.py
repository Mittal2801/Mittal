choice=int(input("enter your choice "))
print("your choice is ",choice)


if choice==1:
    print("Your choice is 1 now convert Fehrenheit to Celcius")
    f=int(input("enter value of fehrenheit="))
    print("Fehrenheit=",f)
    c=(f-32)*5/9
    print("Fehrenheit to Celsius=",c)
    
else:
    print("Your choice is 2 now convert Fehrenheit to Celcius")
    c=int(input("enter value of celcius="))
    print("Celcius=",c)
    f=(c *9/5)+32
    print("Celsius to Fehrenheit=",f)