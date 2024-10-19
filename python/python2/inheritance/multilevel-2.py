class Person:
    def __init__(self):
        print('Person - Hii')
    def age(self,a):
        print('Printing the age:',a)
        
class Father(Person):
    def __init__(self):
        print('Father - Hii')
        super().__init__()
    def age(self,a):
        print('Printing the age(Father):',a)
        super().age(a+21)
        
class Mother(Father):
    def __init__(self):
        print('Mother - Hii')
        super().__init__()
    def age(self,a):
        print('Printing the age(Mother):',a)
        super().age(a+5)
        
#Main function
o = Mother()
o.age(30)