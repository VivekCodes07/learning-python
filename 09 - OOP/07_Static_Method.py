# Static Method:
# Problem: Add a static method to the Car class that returns a general dedcription of a car.


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + " 🚗"

    def display_detail(self):
        return f"Car brand: {self.__brand} & Model: {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
       return "Electric Charge"
    

my_car = Car("Tata", "Safari")

# print(my_car.general_description())
print(Car.general_description())