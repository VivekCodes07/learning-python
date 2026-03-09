def average(a = 9, b = 7):
    print(f"The average is: {(a + b) / 2}")

# average(1, 5) 
average(5) 
average(b = 9)


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")          # Uses default: "Hello, Alice!"
greet("Bob", "Hi")      # Overrides default: "Hi, Bob!"
