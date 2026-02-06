# Write a function to find the factorial of n. (n is the parameter)

def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


number = int(input("Enter the the number whose factorial you want: "))

print(f"Result: {factorial(number)}")