# Write a function to calculate and return the square of a number.

num = int(input("Enter the number whose square you want: "))

#function definition
def square(number):
    return number ** 2

square_result = square(num)
print(f"Square result: {square_result}")