# Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(valOne, valTwo):
    return valOne * valTwo

value1 = input("Enter a number or string: ")
value2 = input("Enter a number or string: ")

# Convert to int only if the input is a number
if value1.isdigit():
    value1 = int(value1)

if value2.isdigit():
    value2 = int(value2)
    
result = multiply(value1, value2)
print(f"Result: {result}")