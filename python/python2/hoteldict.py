print("\t\t\t\t**********This is admin side**********")\
    
starter={}
main={}
desert={}

rpt=1
while rpt==1:
    print("\t\t\t\tPress 1 for Starter \n\t\t\t\tPress 2 for Main Course \n\t\t\t\tPress 3 for Desert")
    choice=int(input("Enter any number 1 or 2 or 3:"))

    if choice==1:
        print("\t\t\t\t**********STARTER**********")
        si=int(input("How many item you want in starter:"))
        for i in range(si):
            item=input("\t\t\t\tEnter Item Name:")
            price=int(input("\t\t\t\tEnter Item Price:"))
            starter[item]=price
        print("Starter:-",starter)

        srpt=1
        while srpt==1:
            modify=input("\n\t\t\t\tDo you want to modify? y/n :")
            if modify=='y':
                mstarter=1
                while mstarter==1:
                    print("\n\t\t\t\tPress 1 for Insert \n\t\t\t\tPress 2 for Delete \n\t\t\t\tPress 3 for Index using Delete")
                    id=int(input("\nEnter any number 1 or 2 or 3 or 4:"))
                    if id==1:
                        how=int(input("\nHow many item you want in starter:"))
                        for i in range(how):
                            sitem=input("\n\t\t\t\tEnter Item Name:")
                            sprice=int(input("\t\t\t\tEnter Item Price:"))
                            starter[sitem]=sprice
                        print("\nStarter:-",starter)
                    
                    elif id==2:
                        starter.popitem()
                        print("Starter:-",starter)
                    
                    
                    elif id==3:
                        key=input("\n\t\t\t\tEnter item name you want to delete:")
                        starter.pop(key)
                        print("Starter:-",starter)
                        
                    elif id==4:
                        exit()
                        
                    mstarter=int(input("\n\t\tDo you want to again modify starter?Press 1:"))
                    
            elif modify=='n':
                print("Starter:-",starter)
            srpt=int(input("\n\t\t\t\tYou again repeat starter?Press 1:"))
                    
    if choice==2:
        print("\t\t\t\t**********Main Course**********")
        mi=int(input("How many item you want in Main Course:"))
        for i in range(mi):
            item=input("\t\t\t\tEnter Item Name:")
            price=int(input("\t\t\t\tEnter Item Price:"))
            main[item]=price
        print("Main Course:-",main)

        mrpt=1
        while mrpt==1:
            modify=input("\n\t\t\t\tDo you want to modify? y/n :")
            if modify=='y':
                mmain=1
                while mmain==1:
                    print("\n\t\t\t\tPress 1 for Insert \n\t\t\t\tPress 2 for Delete \n\t\t\t\tPress 3 for Index using Delete \n\t\t\t\tPress 4 for Exit")
                    id=int(input("\nEnter any number 1 or 2 or 3 or 4:"))
                    if id==1:
                        how=int(input("\nHow many item you want in Main course:"))
                        for i in range(how):
                            mitem=input("\n\t\t\t\tEnter Item Name:")
                            mprice=int(input("\t\t\t\tEnter Item Price:"))
                            main[mitem]=mprice
                        print("\nMain Course:-",main)
                    
                    elif id==2:
                        how=int(input("How many item you want to delete in main course:"))
                        for i in range(how):
                            mitem=input("Enter Item Name:")
                            mprice=int(input("Enter Item Price:"))
                        main.popitem()
                        print("Main Course:-",main)
                    
                    
                    elif id==3:
                        key=input("Enter item name you want to delete:")
                        main.pop(key)
                        print("Main course:-",main)
                        
                    elif id==4:
                        exit()
                        
                    mmain=int(input("\n\t\tDo you want to again modify main course?Press 1:"))
                    
            elif modify=='n':
                print("Main Course:-",main)
            mrpt=int(input("\n\t\t\t\tYou again repeat main course?Press 1:"))
            
    if choice==3:
        di=int(input("How many item you want in Desert:"))
        for i in range(di):
            item=input("\t\t\t\tEnter Item Name:")
            price=int(input("\t\t\t\tEnter Item Price:"))
            desert[item]=price
        print("Desert:-",desert)

        drpt=1
        while drpt==1:
            modify=input("\n\t\t\t\tDo you want to modify? y/n :")
            if modify=='y':
                mdesert=1
                while mdesert==1:
                    print("\n\t\t\t\tPress 1 for Insert \n\t\t\t\tPress 2 for Delete \n\t\t\t\tPress 3 for Index using Delete \n\t\t\t\tPress 4 for Exit")
                    id=int(input("\nEnter any number 1 or 2 or 3 or 4:"))
                    if id==1:
                        how=int(input("\nHow many item you want in Desert:"))
                        for i in range(how):
                            ditem=input("\n\t\t\t\tEnter Item Name:")
                            dprice=int(input("\t\t\t\tEnter Item Price:"))
                            desert[ditem]=dprice
                        print("\nDesert:-",desert)
                    
                    elif id==2:
                        how=int(input("How many item you want to delete in Desert:"))
                        for i in range(how):
                            mitem=input("Enter Item Name:")
                            mprice=int(input("Enter Item Price:"))
                            
                        desert.popitem()
                        print("Desert:-",desert)
                    
                    
                    elif id==3:
                        key=input("Enter item name you want to delete:")
                        desert.pop(key)
                        print("Desert:-",desert)
                        
                    elif id==4:
                        exit()
                        
                    mdesert=int(input("\n\t\tDo you want to again modify desert?Press 1:"))
                    
            elif modify=='n':
                print("Desert:-",desert)
            drpt=int(input("\n\t\t\t\tYou again repeat desser?Press 1:"))
            
    rpt=int(input("\n\t\t\t\twant to repeat? press 1"))      
print("Menu of starter=",starter)
print("Menu of main course=",main)
print("Menu of desert=",desert)

print("---------This is User Side-------------")

name=input("Enter Your Name:")
print("\n\t\t\t\t*****Welcome to Mittal's hotel",name,"*****")
orpt=1
while orpt==1:

    print("\n\t\t\t\tPress 1 for Starter \n\t\t\t\tPress 2 for Main Course \n\t\t\t\tPress 3 for Desert")
    choice=int(input("Enter any number 1 or 2 or 3:"))

    ostarter={}
    omain={}
    odesert={}


    if choice==1:
        print("\n\t\t\t\t*****STARTER*****")
        print("\n\t\t\t\tMenu of Starter:-",starter)
        no=int(input("How many item you want in starter order:"))
        count = 0
        # for i in range(no):
        while no > count:
            oitem=input("\t\t\t\tEnter Item Name:-")
            if oitem in starter:
                ostarter[oitem]=price
                count += 1       
            else:
                print("\t\t\t\tItem is not available")
        print("Your starter order:-",ostarter)
            
        update=input("\n\t\t\t\tDo you update this order?y/n:")
        sorpt=1
        while sorpt==1:
                if update=='y':
                    id=int(input("\n\t\t\t\tPress 1 for Insert \n\t\t\t\tPress 2 for Delete \n\t\t\t\tPress 3 for Index Using Delete \n\t\t\t\tPress 4 for Exit"))  
                    if id==1:
                        si=int(input("how many items you again want in starter:"))
                        count = 0
                        # for i in range(si):
                        while si > count:
                            oitem=input("\t\t\t\tenter item name:")
                            if oitem in starter:
                                ostarter[oitem]=price
                                count += 1
                            else:
                                print("\t\t\t\tItem is not available")
                            
                        print("Updated starter:-",ostarter)
                        
                    elif id==2:
                            ostarter.popitem()
                            print("Updated Starter:-",ostarter)
                            
                            
                    elif id==3:
                        key=input("\n\t\t\t\tEnter any item name you want to delete:")
                        ostarter.pop(key)
                        print("Updated Starter:-",ostarter)
                    elif id==4:
                        exit()
                        
                elif update=='n':
                    print("Starter:-",ostarter)
                sorpt=int(input("\n\t\t\t\twant to again update starter ?press 1"))
                
    if choice==2:
        print("\n\t\t\t\t*****MAIN COURCE*****")
        print("\n\t\t\t\tMenu of Main Course:-",main)
        no=int(input("How many item you want in Main Course order:"))
        count = 0
        # for i in range(no):
        while no > count:
            oitem=input("\t\t\t\tEnter Item Name:-")
            if oitem in main:
                omain[oitem]=price
                count += 1
            else:
                print("\t\t\t\tItem is not available")
        print("Your Main Course order:-",omain)
            
        update=input("\n\t\t\t\tDo you update this order?y/n:")
        morpt=1
        while morpt==1:
            if update=='y':
                id=int(input("\n\t\t\t\tPress 1 for Insert \n\t\t\t\tPress 2 for Delete \n\t\t\t\tPress 3 for Index Using Delete \n\t\t\t\tPress 4 for Exit"))  
                if id==1:
                    mi=int(input("how many items you again want in main course:"))
                    count = 0
                    # for i in range(mi):
                    while mi > count:
                        oitem=input("\t\t\t\tenter item name:")
                        if oitem in main:
                            omain[oitem]=price
                            count += 1
                        else:
                            print("\t\t\t\tItem is not available")
                                                    
                    print("Updated Main Course:-",omain)
                        
                elif  id==2:
                    omain.popitem()
                    print("Updated Main Course:-",omain)
                            
                            
                elif id==3:
                    key=input("\n\t\t\t\tEnter item name you want to delete:")
                    omain.pop(key)
                    print("Updated Main Course:-",omain)
                                
                elif id==4:
                    exit()
                        
            elif update=='n':
                print("Main Course:-",omain)
            morpt=int(input("\n\t\t\t\twant to again update main course?press 1"))
    
    if choice==3:
        print("\n\t\t\t\t*****DESERT*****")
        print("\n\t\t\t\tMenu of Desert:-",desert)
        no=int(input("How many item you want in Desert order:"))
        count=0
        # for i in range(no):
        while no > count:
            oitem=input("\t\t\t\tEnter Item Name:-")
            if oitem in desert:
                odesert[oitem]=price
                count +=1
            else:
                print("\t\t\t\tItem is not available")
        print("Your Desert order:-",odesert)
            
        update=input("\n\t\t\t\tDo you update this order?y/n:")
        dorpt=1
        while dorpt==1:
            if update=='y':
                id=int(input("\n\t\t\t\tPress 1 for Insert \n\t\t\t\tPress 2 for Delete \n\t\t\t\tPress 3 for Index Using Delete \n\t\t\t\tPress 4 for Exit"))  
                if id==1:
                    di=int(input("how many items you again want in desert:"))
                    count = 0
                    # for i in range(di):
                    while di > count:
                        if oitem in desert:
                            oitem=input("\t\t\t\tenter item:")
                            odesert[oitem]=price
                        else:
                            print("\t\t\t\tItem is not available")
                                
                                            
                    print("Updated Desert:-",odesert)
                        
                elif id==2:
                    odesert.popitem()
                    print("Updated Desert:-",odesert)
                            
                            
                elif id==3:
                    key=input("\n\t\t\t\tEnter any item name you want to delete:")
                    odesert.pop(key)
                    print("Updated Desert:-",odesert)
                                
                                
                elif id==4:
                    exit()
                                
            elif update=='n':
                print("Desert:-",odesert)
            dorpt=int(input("\n\t\t\t\twant to again update desert?press 1"))

    orpt=int(input("\n\t\t\t\tYou again repeat?Press 1"))

stotal=0
mtotal=0
dtotal=0

print("\n\t\t\t\t**********Your Bill**********")

for i in ostarter:
    ans=ostarter[i]
    stotal=stotal+ans
print("Starter bill=",stotal)
    
for i in omain:
    ans=omain[i]
    mtotal=mtotal+ans
print("Main Course bill=",mtotal)
    
for i in odesert:
    ans=odesert[i]
    dtotal=dtotal+ans
print("Desert bill=",dtotal)
    
maintotal=stotal+mtotal+dtotal





print("\n\t\t\t\t**********your final order is**********")    
print("order of starter=",ostarter)
print("order of main course=",omain)
print("order of desert=",odesert)       
print("Final Bill:-",maintotal)
print("\n\t\t\t\t***********Thank You" ,name,"for visiting my hotel**************")                                                        