class student:
    marks = 10
    @classmethod
    def modify(cls,name):
        print("{} scored {} marks".format(name,cls.marks))
student.modify("Sanjay")
student.modify("Ajay")