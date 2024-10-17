# class Talent:
#     a = 5
#     b = 15
    
# x = Talent
# print(x.b)

class item:
    def __init__(self,name,surname):
        self.xyz = name
        self.abc = surname
        
    def show(self):
        print("your name is " + self.xyz)
        print("your surname is " +self.abc)
        print("your full name is " +self.xyz+ ""+self.abc)
        
        
a = item('vidhi','nagar')
b = item('mittal','prajapati')
print(a.xyz)
a.show()
print(b.abc)
b.show()