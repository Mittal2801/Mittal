class myclass:
    n = 0
    def __init__(self):
        myclass.n += 1
    @staticmethod
    def noo():
        print(myclass.n)
    
one = myclass()
two = myclass()
three = myclass()
myclass.noo()