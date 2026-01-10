a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus → 1
print(a ** b)  # Exponentiation → 1000


x = 3.14
y = -4
z = 5

# Round off - round()
print(f"Before rounding, x = {x}")
result = round(x)
print(f"After rounding, x = {result}")

# Absolute value - abs()
result2 = abs(y)
print(f"Absolute value of y = {result2}")

# pow()
result3 = pow(z, 2)
print(f"5 rasied to the power 2: {result3}")

# max(x, y, z)
resultMax = max(x, y, z)
resultMin = min(x, y, z)

print(f"Maximum value bw x, y, z: {resultMax}")
print(f"Minimum value bw x, y, z: {resultMin}")


import math

print(f"Value of PI = {math.pi}")
print(f"Square-root of a 2 = {math.sqrt(2)}")

num = 5.3
print("math.ceil(5.3): ", math.ceil(num))
print("math.floor(5.3): ", math.floor(num))


# Find circumference of a circle by taking input from the user.

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"Circumference of circle with radius {radius} cm = {round(circumference, 2)}cm^2")


# Calculate area of a cicle

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"Area of circle = {round(area, 2)}cm^2")