class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print("name:",self.firstname,"surname:",self.lastname)
        
class Student(Person):
    pass


x = Student("Talent","Computer")
x.printname()