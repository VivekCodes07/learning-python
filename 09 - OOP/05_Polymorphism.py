# Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + " 🚗"

    def display_detail(self):
        return f"Car brand: {self.__brand} & Model: {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
       return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(f"Tesla's fuel type: {my_tesla.fuel_type()}")

safari = Car("Tata", "Safari")
print(f"Tata's fuel type: {safari.fuel_type()}")