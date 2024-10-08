cardBal=1000
play=1

while play == 1:
    print("your card balance is ",cardBal)
    choice=int(input("Rs.500 for car racing press 1 \n Rs.750 for cycling press 2 \n Rs.150 for jumping press 3"))
    if  choice == 1:
        if cardBal >= 500:
            print("Welcome to Car Racing")
            cardBal -=500
        else:
            print("Insufficient balance please top up for play")           
    elif  choice == 2:
        if cardBal >= 750:
            print("Welcome to Cycling")
            cardBal -=750
        else:
            print("Insufficient balance please top up for play") 
    elif  choice == 3:
        if cardBal >= 150:
            print("Welcome to Jumping")
            cardBal -=150
        else:
            print("Insufficient balance please top up for play")           
    else:
         print("Wrong Choice")
         
    print("your last balance is ",cardBal)
    
    play=int(input("Do you want to play another game? press 1 for continue and other to exit"))