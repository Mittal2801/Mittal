class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print("name:",self.firstname,"surname:",self.lastname)
        
class Student(Person):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.statingsalary = salary
        
        
x = Student("Mittal","Prajapati","35000")
x.printname()
print("salary:",x.statingsalary)
