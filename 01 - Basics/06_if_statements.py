# if = Do something If some condition is True
# Else do something else

#Example 1:
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to drive")
elif age < 0:
    print("You haven't been born yet")
elif age >= 100:
    print("You are too old to drive")
else:
    print("Wait till you're 18")

#Example 2:
response = input("Would you like to have food? (Y/N): ")

if response == "Y":
    print("Serving in two minutes...")
else:
    print("No food for you...")

#Example 3:
online = True

if online:
    print("The user is online")
else:
    print("The user is offline")