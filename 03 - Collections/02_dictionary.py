# A dictionary is a collection of key–value pairs.
# Dictionary is mutable — you can change it anytime

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print(student.get("name")) # Safe way (recommended)
print(student["age"])

student["name"] = "Vivek"
print(student)


for detail in student:
    print(f"{detail}: {student[detail]}")

if "course" in student:
    print("Opted for Python")

# Adding & Updating Values
student["cgpa"] = 9.2
print(student)
student["course"] = "JavaScript"


# Removing Elements

# Remove specific key
student.pop("age") 
print(student)

# Remove last inserted item
student.popitem()
print(student)


# Nested Dictionary

students = {
    "student1": {
        "name": "Michael Jackson",
        "age": 20,
        "marks": 92
    },
    "student2": {
        "name": "John Cena",
        "age": 20,
        "marks": 88
    }
}

print(students["student1"]["name"])


squared_num = {x:x**2 for x in range(6)}

print(squared_num)
squared_num.clear()
print(squared_num)