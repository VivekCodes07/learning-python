class Car:
    # Constructor -> It initializes (sets up) the object with values.
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    # Method
    def display_detail(self):
        return f"Car brand: {self.brand} & Model: {self.model}"


my_car = Car("Volkswagen", "Virtus GT")
print(my_car.brand)
print(my_car.display_detail())

my_new_car = Car("Skoda", "Slavia")
print(f"My new car is {my_new_car.brand}")