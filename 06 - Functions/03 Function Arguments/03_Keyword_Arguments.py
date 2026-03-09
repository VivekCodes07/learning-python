def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet("John", last_name="Cena")

greet(last_name="Lesnar", first_name="Brock") # Order does not matter

# Incorrect: Positional argument follows keyword argument
# greet(first_name="John", "Doe") # This will raise a SyntaxErro