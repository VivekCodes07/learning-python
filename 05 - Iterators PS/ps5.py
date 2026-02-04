# Given a string find the first non-repeated character

input_str = "teeter"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print(f"The first Non-repeated character: {char}")
        break