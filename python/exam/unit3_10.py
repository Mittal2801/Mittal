class square:
    def __init__(self,x):
        self.x = x
    def area(self):
        print(self.x * self.x)
class rectangle(square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    def area(self):
        super().area()
        print(self.x * self.y)
        
a,b = [float(x) for x in input("Enter l and b:").split()]
r = rectangle(a,b)
r.area()