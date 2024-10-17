def bill(unit):
    if unit<=50:
        ans=unit*0.50
        print("ans=",ans)
       
        
    elif unit>50 and unit<150:
        ans=25+(unit-50)*0.75
        print("ans=",ans)
        
        
    elif unit>150 and unit<250:
        ans=25+75+(unit-150)*1.00
        print("ans=",ans)
        
        
    else:
        ans=25+75+100+(unit-250)*1.50
        print("ans=",ans)
       
       
    extra=ans*0.20
    print("extra charge=",extra)
    
    ans = ans + extra
    print("final bill",ans)
    
        
    




        
        
unit=int(input("enter unit:"))

bill(unit)




