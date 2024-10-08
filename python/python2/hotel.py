num=int(input("how many times you print name:"))
i=1
list=[]

while num>=i:
        name=(input("enter name:"))
        list.append(name)
        i=i+1
        
        
print(list)

menu=1

while menu==1:
    choice=int(input("press 1 for length  \npress 2 for append  \npress 3 for pop \npress 4 for remove \npress 5 for clear \npress 6 for delete"))
    
    if choice==1:
        print(len(list))
    
    elif choice==2:
        no=int(input("press 1 for append  \n press 2 for index using insert "))
        if no==1:
            new=input("enter any item:")
            list.append(new)
            print(list)
        elif no==2:
            inum=int(input("enter any index number:"))
            item=input("enter any item:")
            list.insert(inum,item)
            print(list)
        else:
            print("Invalid number")
            
    elif choice==3:
        no=int(input("press 1 for pop  \n press 2 for index using pop "))
        if no==1:
            list.pop()
            print(list)
        elif no==2:
            inum=int(input("enter any index number:"))
            list.pop(inum)
            print(list)
        else:
            print("Invalid number")
            
    elif choice==4:
        print(list)
        select=input("choose one item in your list:")
        list.remove(select)
        print(list)
        
    elif choice==5:
        list.clear()
        print("list=",list)
        
    elif choice==6:
        del[list]
        print(list)
        
        

        
menu=int(input("are you repeat_press 1 otherwise another number:"))
        
        
        
        
            
        
    



