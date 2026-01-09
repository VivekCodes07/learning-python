# Variable =  A container for a value (string, integer, float, boolean) 

# A variables behaves as if it was the value it contains.

# Strings
first_name = "Vivek"
last_name = "Kr"
email = "vivek@google.com"

print(first_name)
print(f"Hello {first_name}")


#Integers
age = 19
quantity = 3
num_of_students = 30


print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")


#Float
price = 10.99
gpa = 9.5
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} km")


#Boolean
is_student = True

if is_student:
    print("You are eligible for student discount")
else:
    print("You are not eligible for student discount")


is_online = True

if is_online:
    print("The user is online")
else: 
    print("The user is offine")