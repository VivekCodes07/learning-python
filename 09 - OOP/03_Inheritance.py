# Create an Electric Car class that inherits from the Car class and has an additional attribute battery_size.

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

print(my_tesla.display_detail())