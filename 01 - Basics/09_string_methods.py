name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

length_of_str = len(name)
print(f"Length of the String: {length_of_str}")

position = name.find("e")
print(f"Position of 'e': {position}")

print(f"Name: {name.capitalize()}")
print(f"Name: {name.upper()}")
print(f"Name: {name.lower()}")

# result = name.isdigit()
result = name.isalpha()
print(result)

count = phone_number.count("6")
print(f"Number of times 6 is occuring in your phone number: {count}")

phone_number = phone_number.replace("-", "")
print(f"Phone number: {phone_number}")

# print(help(str)) -> Returns all the string methods available to us


# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if (len(username)) > 12:
    print("Your username can't be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can't contain be more than 12 characters")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    (print(f"Welcome {username}"))