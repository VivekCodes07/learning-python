# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = input("Enter the color of your banana: ").lower()

if color == "green":
    print("Quality status: Unripe")
elif color == "yellow":
    print("Quality status: Ripe")
elif color == "brown":
    print("Quality status: Overripe")
else:
    print("Unknown color. Please enter green, yellow, or brown.")
