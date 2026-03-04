# Class inheritance and isinstance() function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and Electric Car.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    # Method
    def display_detail(self):
        return f"Car brand: {self.brand} & Model: {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))