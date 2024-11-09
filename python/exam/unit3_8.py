class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.salary = sal
        
    def display(self):
        print("Id=",self.id)
        print("Name=",self.name)
        print("Salary=",self.salary)
        
class myclass:
    @staticmethod
    def mymethod(e):
        e.salary += 100
        e.display()
        
e = Emp(1001,"Raj Kumar",12000.75)
myclass.mymethod(e)