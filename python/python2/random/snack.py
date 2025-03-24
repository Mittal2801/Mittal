import random

dice = [1,2,3,4,5,6]
snack = {4:2,5:1,8:2,9:4}
leader = {3:7,2:5,1:4,6:9}
player1 = 0
player2 = 0
player3 = 0
player4 = 0
game = True
name1 = input("please enter your name:")
name2 = input("please enter your name:")
name3 = input("please enter your name:")    
name4 = input("please enter your name:")    

while game == True:
    p1 = (name1,"-press 1 for play game:")
    if p1 == 1:
        num = random.choice(dice)
        print("Dice=",num)
        player1 += num
        print("Player1 Score=",player1)
        for i in snack:
            # print(i)
            if i == player1:
                player1 = snack[i]
                print("bitten")
                print("After bitten=",player1)
        
        for i in leader:
            # print(i)
            if i == player1:
                player1 = leader[i]
                print("leader")
                print("After leader=",player1)
        if player1 >= 10:
            print("1 winner")
            break
        
    p2 = (name2,"Player2-press 2 for play game:")
    if p2 == 2:
        num = random.choice(dice)
        print("Dice=",num)
        player2 += num
        print("Player2 Score=",player2)
        for i in snack:
            if i == player2:
                player2 = snack[i]
                print("bitten")
                print("After bitten=",player2)
                
        for i in leader:
            # print(i)
            if i == player2:
                player2 = leader[i]
                print("leader")
                print("After leader=",player2)
        if player2 >= 10:
            print("2 winner")
            break
        
    p3 = input(name3,"Player1-press 3 for play game:")
    if p3 == 3:
        num = random.choice(dice)
        print("Dice=",num)
        player3 += num
        print("Player3 Score=",player1)
        for i in snack:
            # print(i)
            if i == player3:
                player3 = snack[i]
                print("bitten")
                print("After bitten=",player3)
        
        for i in leader:
            # print(i)
            if i == player3:
                player3 = leader[i]
                print("leader")
                print("After leader=",player3)
        if player3 >= 10:
            print("3 winner")
            break
        
    p4 = input(name4,"Player1-press 4 for play game:")
    if p4 == 4:
        num = random.choice(dice)
        print("Dice=",num)
        player4 += num
        print("Play er4 Score=",player4)
        for i in snack:
            # print(i)
            if i == player4:
                player4 = snack[i]
                print("bitten")
                print("After bitten=",player4)
        
        for i in leader:
            # print(i)
            if i == player4:
                player4 = leader[i]
                print("leader")
                print("After leader=",player4)
        if player4 >= 10:
            print("4 winner")
            break