# Create a funcion that takes two numbers as parameters and returns their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def add(a, b):
    return a + b

result = add(num1, num2)
print(f"Sum: {result}")