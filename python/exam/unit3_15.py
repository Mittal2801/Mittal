class Dog:
    def bark(self):
        print("Bow Bow")
class Duck:
    def talk(self):
        print("Quack Quack")
class Human:
    def talk(self):
        print("Hello,Hi")

def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
    else:
        print("Wrong object passed")
        
x = Duck()
call_talk(x)
x = Human()
call_talk(x)
x = Dog()
call_talk(x)