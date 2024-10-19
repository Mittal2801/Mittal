class length:
    l =0 

class width:
    b = 0
    
class rect_area(length,width):
    def r_area(self):
        print("The area of rectangle with length "+str(self.l)+"units of width "+str(self.b)+"units is "+str(self.l * self.b)+"sq.units.")
        
o = rect_area()
o.l = int(input("Enter length:"))
o.b = int(input("Enter width:"))
o.r_area()