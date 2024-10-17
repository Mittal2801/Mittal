class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print("name:",self.firstname,"age:",self.lastname)
        
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)#super().__init__(fname,lname)
        
        
        
name = input("enter your name:")
age = int(input("enter your age:"))
x = Student(name,age)
x.printname()