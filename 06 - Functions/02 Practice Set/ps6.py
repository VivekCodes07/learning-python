# Create a lambda fucntion to compute the cube of a number.

cube = lambda x: x ** 3

num = int(input("Enter the number whose cube you want: "))

print(f"Result: {cube(num)}")
