# Conditional expression -> A one-line shortcut for the if-else statement (ternary operator).
# Print or assign one of two values based on a condtion x else y

num = 5

print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 6
b = 7

max_num = a if (a > b) else b
min_num = b if (b < a) else a

print(f"Maximum: {max_num}, Minimum: {min_num}")