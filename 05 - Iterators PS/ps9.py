# Check if all the elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

fruits = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for fruit in fruits:
    if fruit in unique_items:
        print(f"The duplicate value = {fruit}")
        break
    else:
        unique_items.add(fruit)
