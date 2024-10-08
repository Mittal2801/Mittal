import random

min=int(input("Enter lower bound:"))
max=int(input("Enter upper bound:"))

guess=random.randrange(min,max)
# print(guess)

for i in range(0,7):

    if i==1:
        num=int(input("Enter number:"))

        
        if num > guess:
            print("You choose lower value")
            print("4 chances left")
        elif num < guess:
            print("You choose high value")
            print("4 chances left")

        elif num == guess:
            print("Guess number=",guess,"Your number=",num)
            print("You won")
            break
            
    if i==2:
        num=int(input("Enter number:"))

        
        if num > guess:
            print("You choose lower value")
            print("3 chances left")

        elif num < guess:
            print("You choose high value")
            print("3 chances left")

        elif num == guess:
            print("Guess number=",guess,"Your number=",num)
            print("You won")
            break
                
    if i==3:
        num=int(input("Enter number:"))

        
        if num > guess:
            print("You choose lower value")
            print("2 chances left")

        elif num < guess:
            print("You choose high value")
            print("2 chances left")

        elif num == guess:
            print("Guess number=",guess,"Your number=",num)
            print("You won")
            break
                
    if i==4:
        num=int(input("Enter number:"))

        
        if num > guess:
            print("You choose lower value")
            print("1 chances left")

            
        elif num < guess:
            print("You choose high value")
            print("1 chances left")

        elif num == guess:
            print("Guess number=",guess,"Your number=",num)
            print("You won")
            break
                
    if i==5:
        num=int(input("Enter number:"))

        
        if num > guess:
            print("You choose lower value")
            print("0 chances left")

        elif num < guess:
            print("You choose high value")
            print("0 chances left")

        elif num == guess:
            print("Guess number=",guess,"Your number=",num)
            print("You won")
            break    
        
else:
    print("Sorry!!You try again this game")     