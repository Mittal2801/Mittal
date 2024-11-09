class a:
    def method(self):
        print("A class method")
        super().method()
        
class b:
    def method(self):
        print("B class method")
        super().method()
        
class c:
    def method(self):
        print("C class method")
        super().method()
        
class x(a,b):
    def method(self):
        print("X class method")
        super().method()
        
class y(b,c):
    def method(self):
        print("Y class method")
        super().method()
        
class p(x,y,c):
    def method(self):
        print("P class method")
        super().method()
        
newp = p()
print(p.mro())
newp.method()