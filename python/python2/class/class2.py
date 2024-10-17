class Tcit:
    x = 5
    def __init__(self,roll,name):
        self.id = roll
        self.name = name
    def hello(self):
        print("hello")
    def display(self):
        print("The Roll no is ",self.id," and Name is ",self.name)
    def mittal(self):
        print(self.id*5)
        
        
        
first_obj = Tcit(11,"talent")
print(first_obj.x*5)
first_obj.hello()
first_obj.display()
first_obj.mittal()