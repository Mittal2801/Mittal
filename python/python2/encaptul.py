class Car:
    def __init__(self,make,model):
        self.__make = make #Private attribute
        self.__model = model #Private attribute
        
    def get_make(self):
        return self.__make
    
    def set_make(self,make):
        self.__make = make
        
    def get_model(self):
        return self.__model
    
    def set_model(self,model):
        self.__model = model
        
    def display_info(self):
        print(f"Car: {self.__make} {self.__model}")
        
my_car = Car("Toyota","Corolla")


print(my_car.get_make())
print(my_car.get_model())

my_car.set_make("Honda")
my_car.set_model("Civic")

my_car.display_info()

