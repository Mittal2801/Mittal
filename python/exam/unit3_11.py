class teacher:
    def __init__(self):
        self.id = 1001
    def display(self):
        print("Teachers id:",self.id)
class student(teacher):
    def __init__(self):
        self.id = 1
    def display(self):
        print("Students id:",self.id)

s = student()
s.display()