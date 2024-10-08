print("-*-*-*-*-*-This is Admin Side-*-*-*-*-*-")

starter=[]
main=[]
desert=[]
count=0

rpt=1

while rpt==1:
    print("press 1 for starter \npress 2 for main \npress 3 for desert")

    choice=int(input("press 1 or 2 or 3:"))
    print("your choice is ",choice)
    
    if choice==1:
        
            si=int(input("how many items you want in starter:"))
            for i in range(si):
                        item=input("enter item:")
                        starter.append(item)
            print(starter)

            srpt=1
            while srpt==1:
                id=int(input("press 1 for insert item\npress 2 for delete item"))
                if id==1:
                    si=int(input("how many items you want in starter:"))
                    no=int(input("press 1 for append \npress 2 for index using insert"))
                    if no==1:
                        for i in range(si):
                            item=input("enter item:")
                            starter.append(item)
                        print(starter)
                        count+=1
                    elif no==2:
                        for i in range(si):
                                istarter=int(input("enter any index number:"))
                                item=input("enter any item name:")
                                starter.insert(istarter,item)
                        print(starter)
                        count+=1

                elif id==2:
                    no=int(input("press 1 for delete item \npress 2 for index using delete item"))
                    if no==1:
                        starter.pop()
                        print(starter)
                        count+=1

                    elif no==2:
                        istarter=int(input("enter any index number:"))
                        starter.pop(istarter)
                        print(starter)
                        count+=1
                srpt=int(input("want to repeat starter? press 1"))       
           
                     


    if choice==2:
        
            mi=int(input("how many items you want in main course:"))
            for i in range(mi):
                        item=input("enter item:")
                        main.append(item)
            print(main)


            mrpt=1
            while mrpt==1:
                id=int(input("press 1 for insert item\npress 2 for delete item"))
                if id==1:
                    mi=int(input("how many items you want in main course:"))
                    no=int(input("press 1 for append \npress 2 for index using insert"))
                    if no==1:
                        for i in range(mi):
                            item=input("enter item:")
                            main.append(item)
                        print(main)
                        count+=1
                    elif no==2:
                        for i in range(mi):
                            imain=int(input("enter any index number:"))
                            item=input("enter any item name:")
                            main.insert(imain,item)
                        print(main)
                        count+=1

                elif id==2:
                    no=int(input("press 1 for delete item \npress 2 for index using delete item"))
                    if no==1:
                        main.pop()
                        print(main)
                        count+=1

                    elif no==2:
                        imain=int(input("enter any index number:"))
                        main.pop(imain)
                        print(main)
                        count+=1
                mrpt=int(input("want to repeat main course?press 1"))
                
    if choice==3:
        
            di=int(input("how many items you want in desert:"))
            for i in range(di):
                        item=input("enter item:")
                        desert.append(item)
            print(desert)

            drpt=1
            while drpt==1:
                id=int(input("press 1 for insert item\npress 2 for delete item"))
                if id==1:
                    di=int(input("how many items you want in desert course:"))
                    no=int(input("press 1 for append \npress 2 for index using insert"))
                    if no==1:
                        for i in range(di):
                            item=input("enter item:")
                            desert.append(item)
                        print(desert)
                        count+=1
                    elif no==2:
                            for i in range(di):
                                    idesert=int(input("enter any index number:"))
                                    item=input("enter any item name:")
                                    desert.insert(idesert,item)
                            print(desert)
                            count+=1

                elif id==2:
                    no=int(input("press 1 for delete item \npress 2 for index using delete item"))
                    if no==1:
                        desert.pop()
                        print(desert)
                        count+=1

                    elif no==2:
                        idesert=int(input("enter any index number:"))
                        desert.pop(idesert)
                        print(desert)
                        count+=1
                drpt=int(input("want to repeat desert?press 1"))
                    
                    
    rpt=int(input("want to repeat? press 1"))      
print("starter=",starter)
print("main course=",main)
print("desert=",desert)


print("-*-*-*-*-*-This is User Side-*-*-*-*-*-")

orpt=1

while orpt==1:
    print("press 1 for starter \npress 2 for main course \npress 3 for desert")

    choice=int(input("enter 1 or 2 or 3:"))
    print("your choice is ",choice)

    ostarter=[]
    omain=[]
    odesert=[]

    if choice==1:
        print("starter=",starter)
        no=int(input("how many item you add in starter order:"))
        for i in range(no):
            item=input("enter item:")
            if item in starter:
                ostarter.append(item)
            else:
                print("item is not available")
                
        print(ostarter)
        sorpt=1
        while sorpt==1:
            yn=input("Do you want to update this starter order? y/n")
            
            
            if yn=='y':
                    id=int(input("press 1 for insert \npress 2 for delete"))
                    if id==1:
                        si=int(input("how many items you want in starter:"))
                        for i in range(si):
                                    item=input("enter item:")
                                    if item in starter:
                                        ostarter.append(item)
                                    else:
                                        print("item is not available")
                                    
                        print(ostarter)
                    
                    elif id==2:
                            no=int(input("press 1 for delete item \npress 2 for index using delete item"))
                            if no==1:
                                ostarter.pop()
                                print(ostarter)

                            elif no==2:
                                istarter=int(input("enter any index number:"))
                                ostarter.pop(istarter)
                                print(ostarter)
            elif yn=='n':
                    print("starter=",ostarter)
            sorpt=int(input("want to again update starter ?press 1"))
            

    if choice==2:
        print("main course=",main)
        no=int(input("how many item you add in main course order:"))
        for i in range(no):
            item=input("enter item:")
            if item in main:
                omain.append(item)
            else:
                print("item is not available")
        print(omain)
        
        
        morpt=1
        while morpt==1:
            yn=input("Do you want to update this main course order? y/n")
            
            if yn=='y':
                    id=int(input("press 1 for insert \npress 2 for delete"))
                    if id==1:
                        mi=int(input("how many items you want in main course:"))
                        for i in range(mi):
                                    item=input("enter item:")
                                    if item in main:
                                        omain.append(item)
                                    else:
                                        print("item is not available")
                        print(omain)
                        
                    elif id==2:
                            no=int(input("press 1 for delete item \npress 2 for index using delete item"))
                            if no==1:
                                omain.pop()
                                print(omain)

                            elif no==2:
                                imain=int(input("enter any index number:"))
                                omain.pop(imain)
                                print(omain)
            elif yn=='n':
                    print("main course=",omain) 
            morpt=int(input("want to again update main course ?press 1"))
                

    if choice==3:
        print("menu of dessert=",desert)
        no=int(input("how many item you add in desert order:"))
        for i in range(no):
            item=input("enter item:")
            if item in desert:
                odesert.append(item)
            else:
                print("item is not available")
        print(odesert)
        
        dorpt=1
        while dorpt==1:
            yn=input("Do you want to update this desert order? y/n")
            
            if yn=='y':
                    id=int(input("press 1 for insert \npress 2 for delete"))
                    if id==1:
                        di=int(input("how many items you want in desert :"))
                        
                        for i in range(di):
                                    item=input("enter item:")
                                    if item in desert:
                                        odesert.append(item)
                                    else:
                                        print("item is not available")
                        print(odesert)
                        
                    elif id==2:
                            no=int(input("press 1 for delete item \npress 2 for index using delete item"))
                            if no==1:
                                odesert.pop()
                                print(odesert)

                            elif no==2:
                                idesert=int(input("enter any index number:"))
                                odesert.pop(idesert)
                                print(odesert)
            elif yn=='n':
                    print("desert=",odesert)
            dorpt=int(input("want to again update desert ?press 1"))

    orpt=int(input("want to repeat order? press 1"))  
print("---------------------your final order is---------------------")    
print("order of starter=",ostarter)
print("order of main course=",omain)
print("order of desert=",odesert)       
print("***********Thank You**************")                                                       