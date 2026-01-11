operator = input("Enter Operator (+, -, *, /): ")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if operator == "+":
    print("Sum = ", num1 + num2)
elif operator == '-':
    print("Difference = ", num1 - num2)
elif operator == '*':
    print("Product = ", num1 * num2)
elif operator == '/':
    print("Division = ", num1 / num2)
else:
    print("Invalid Input")