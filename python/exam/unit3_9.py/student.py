class student:
    def setid(self,id):
        self.id = id
    def getid(self):
        return self.id
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setaddress(self,address):
        self.address = address
    def getaddress(self):
        return self.address
    def setmarks(self,marks):
        self.marks = marks
    def getmarks(self):
        return self.marks
    
import student
s = student()
s.setid(100)
s.setname("Vidhi Nagar")
s.address("City College,satellite,Ahmedabad")
s.setmarks(79)
print(s.getid())
print(s.getname())
print(s.getaddress())
print(s.marks())