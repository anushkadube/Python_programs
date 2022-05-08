
# Classes in pyhton
# init method
# def  __init__
# self holds free space for the name of object

print("Classes in Python \n")

class Cars :
   
    def __init__ (self, brand, model, Type):
        self.brand = brand
        self.model = model
        self.Type = Type
        
car1 = Cars(" Maruti "," Ciaz "," Sedan ")

print("Name of Brand:", car1.brand,"\nName of Model: " , car1.model,"\nType of the car: ",car1.Type)
