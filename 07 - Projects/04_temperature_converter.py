unit = input("Is the tempereature in Celsius or Fahrenheit? (C/F): ")

temp = float(input("Enter the Temperature: "))

if unit == 'C':
    temp = (temp * 9) / 5 + 32
    print(f"The temperature in Fahrenheit is : {temp} °F")
elif unit == 'F':
    temp = ((temp - 32) * 5) / 9
    print(f"The temperature in Celsius is : {temp} °C")
else:
    print(f"{unit} is not a valid unit...")