'''
A tuple in Python is a collection of items that:

. Are ordered
· Are immutable (cannot be changed)
· Can store multiple data types

-> Think of a tuple as a sealed box - once packed, you cannot change what's inside.
'''

my_tuple = (10, 20, 30)
print(my_tuple)


fruits = ("apple", "banana", "mango", "cherry")
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# Slicing
print(fruits[-4:-1])
print(fruits[2: 4])

# Length property 
print(len(fruits)) # 4


# Tuple Methods:

# 1. count() - Returns how many times a value appears in a tuple.

t = (1, 2, 3, 2, 2, 4)
print(t.count(2)) # 3


# 2. index() - Returns the index position of the first occurrence of a value.

t1 = (10, 20, 30, 20)
print(t1.index(20))

tea = ("Herbal", "Earl Grey", "Green", "Oolong")

if "Green" in tea:
    print("I have a green tea")
