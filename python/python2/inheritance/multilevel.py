class class_A:
    def print1(self):
        print("this is class A")
        
class class_B(class_A):
    def print1(self):
        print("this is class B")
        super().print1()
        
class class_C(class_B):
    def print1(self):
        print("this is class C")
        super().print1()
        
obj = class_C()
obj.print1()