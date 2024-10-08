# def add(a1,a2):
#     a3=a1+a2
#     a4=int(input("enter value for multiplication:"))
    
# def mul(a3,a4):
#     a5=a3*a4
#     a6=int(input("enter value for division:"))
    
# # def div(a5,a6):
# #     a7=a5/a6
# #     a8=int(input("enter value for subtraction:"))
    
# # def sub(a7,a8):
# #     a9=a7-a8
# #     a10=int(input("enter value for subtraction:"))
    
# x=int(input("enter x="))
# y=int(input("enter y="))

# ans=sub(x,y)
# print("ans=",ans)





def add(a1,a2):
    ans=a1 + a2
    a3=int(input("enter number for mul"))
    ans2=mul(ans,a3)
    return ans2

def mul(ans,a3):
    multi= ans * a3
    a4=int(input("enter number for div"))
    ans3=div(multi,a4)
    return ans3

def div(multi,a4):
    division=multi/a4
    a5=int(input("enter number for subtraction"))
    ans4=sub(division,a5)
    return ans4
    
def sub(division,a5):
    subtraction=division-a5
    return subtraction
    
    

x=int(input("enter first"))
y=int(input("enter second"))

total=add(x,y)
print(total)

