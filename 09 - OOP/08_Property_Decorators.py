# Property Decorators:
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + " 🚗"

    def display_detail(self):
        return f"Car brand: {self.__brand} & Model: {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def get_model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
       return "Electric Charge"
    

my_car = Car("Tata", "Safari")

print(my_car.get_model)
