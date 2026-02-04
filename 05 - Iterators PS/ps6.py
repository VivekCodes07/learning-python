# Compute the factorial of a number using a while loop

number = int(input("Enter the number whose factorial you want: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    fact = 1
    count = 1
    while (count < number + 1):
        fact = fact * count
        count += 1
    print(f"Factorial of {number} = {fact}") 
