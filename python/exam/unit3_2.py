class student():
    def __init__(self,nm='.',ag=15,m=70):
        self.name = nm
        self.age = ag
        self.marks = m
        
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
        
s = student('Vidhi',19,80)
s.display()

s1 = student('Mittal')
s1.display()