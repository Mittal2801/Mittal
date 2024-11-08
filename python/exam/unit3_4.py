class student:
    #mutator method
    def setname(self,name):
        self.name = name
    #accessor method
    def getname(self):
        return self.name
    
    def setmarks(self,marks):
        self.marks = marks
    def getmarks(self):
        return self.marks
        
n = int(input("how many student?"))
i = 0

while(i<n):
    s = student()
    name=input("enter name:")
    s.setname(name)
    
    marks=int(input("enter marks:"))
    s.setmarks(marks)
    
    print("HI ",s.getname())
    print("Your marks ",s.getmarks())
    i+=1
    print("-----------------------------------")