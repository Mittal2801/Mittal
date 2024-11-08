class student:
    def __init__(self):
        self.name='Mittal'
        self.age=19
        self.marks=80
        
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
        
s = student()
s.display()