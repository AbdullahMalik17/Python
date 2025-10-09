# class CarDetails:
#     def __init__(self,name,color, speed):
#         self.name:str=name
#         self.color=color
#         self.speed=speed
        
#     def accelerate(self,value):
#         self.speed+=value
        
#     def brake(self,value):
#         self.speed-=value
        
#     def get_speed(self):
#         return self.speed
#     def get_details(self):
#         return f"Name: {self.name}, Color: {self.color}, Speed: {self.speed}"
    
# my_car=CarDetails("Mehran","White",120)
# print(my_car.get_details())
# my_car.accelerate(10)
# my_car.brake(20)    
# print(my_car.get_details())

# Now , we are going to make default constructor .
class DogDetails:
    def __init__(self):
        self.name="Unkonwn"
        self.age=0
dog1 = DogDetails()  
dog1.name="Tommy"
print(dog1.name)     
        