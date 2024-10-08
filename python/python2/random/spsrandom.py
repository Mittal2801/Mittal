import random

# print("Press 1 for stone \nPress 2 for Paper \nPress 3 for scissior")



play=1
while play==1:
    user=input("Enter stone or paper or scissior:-")
    print("User choice:-",user)
    
    com=['stone','paper','scissior']
    com=random.choice(com)
    print("Computer choice:-",com)


    if com==user:
        print("tie")
        
    elif com=='stone' and user=='paper':
        print("user is win")
        
    elif com=='stone' and user=='scissior':
        print("computer is win")
        
    elif com=='paper' and user=='stone':
        print("computer is win")
        
    elif com=='paper' and user=='scissior':
        print("user is win")
        
    elif com=='scissior' and user=='stone':
        print("user is win")
        
    elif com=='scissior' and user=='paper':
        print("computer is win")


    play=int(input("You again play this game?Press 1"))