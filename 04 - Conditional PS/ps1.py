# Classify a person's age group: Child (<13), Teenager (13-19), Adult (20-50), Senior (60+)

print("To Know under which category you fall...")

age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
elif 20 <= age <= 60:
    print("Category: Adult")
else:
    print("Category: Senior citizen")