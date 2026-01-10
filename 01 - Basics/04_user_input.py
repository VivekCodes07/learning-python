# input() = A function that prompts the user to enter data
# Returns the entered data as a string

name = input("What is your name? ")
age = int(input("How old are you? "))

"""
age = int(age)
age += 1
"""
print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old")


# Note: You must use 'f' string if you want to use variables


# Exercise 1: Calculate Area of Rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
print(f"Area: {area} m²") # To add superscript -> Alt + 0178


# Exercise 2: Shopping Cart Program

item = input("What item would you like to buy?:")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"Your total bill: ${total}")