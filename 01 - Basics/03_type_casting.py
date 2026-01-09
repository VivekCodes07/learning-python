# Type casting - The process of converting a variable from one data type to another. str(), float(), bool()

name = "Michael Jackson"
age = 19
gpa = 8.5
is_student = True

print(type(name)) #str

gpa = int(gpa)
print(gpa) # 8

print("Before Type casting: age = ", age, "Type: ", type(age))
age = float(age)
print("After Type casting: age = ", age, "Type: ", type(age))