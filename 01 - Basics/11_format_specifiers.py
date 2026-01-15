# format specifiers = (value:flags) format a value based on what flags are inserted

price1 = 3.14159
price2 = 987.657
price3 = 12.34

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

print(f"{'Hi':<10}") # Left align
# Output: 'Hi        '
print(f"{'Hi':^10}") # Center align
# Output: '   Hi   '


name = "Python"
version = 3.12
print("Hello, %s! This is version %.1f" % (name, version))
# Output: Hello, Python! This is version 3.1
