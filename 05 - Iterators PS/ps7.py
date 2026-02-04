# Keep asking the user for input until they enter a number between 1 and 10.

while True:
    value = int(input("Enter value b/w 1 and 10: "))
    if 1 <= value <= 10:
        print("Input STOPPED, since the value was between 1 & 10.")
        break
    else:
        print("Invalid number, Try again...")