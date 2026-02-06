# Write a function to print the elements of a list in a single line. (list is the parameter)

fruits = ["banana", "apple", "litchi", "strawberry", "mango"]

def print_item(list):
    for item in list:
        print(f"{item}", end=" ")
        
print_item(fruits)