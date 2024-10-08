class GFG:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name + " " + self.age)
        
obj = GFG("Mittal","19")
print(obj.show())