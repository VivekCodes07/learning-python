# A collection is a single variable that can store multiple values.

# List = []  
# Ordered (keeps position)
# Changeable (you can add, remove, or update items)
# Allows duplicate values

tea_varities = ["Black", "Green", "Oolong", "White"]

print(tea_varities[0])
print(tea_varities[-1])
print(tea_varities[0:])
print(tea_varities[:2])
tea_varities[1] = "Herbal"
print(tea_varities)
tea_varities[1:3] = ["Ginger", "Masala"]
print(tea_varities)

for tea in tea_varities:
    print(tea)

tea_varities.append("Oolong")

if "Oolong" in tea_varities:
    print("I have Oolong tea")

# append()
nums = [1, 2, 3]
nums.append(4)
# [1, 2, 3, 4]


# pop() – remove by index (default: last)
nums.pop()
print(nums)
# Returns the removed item


# extend() – add MULTIPLE items
nums.extend([5, 6])
print(nums)
# Merges another list


# insert() – add at a specific position
nums.insert(1, 99) # Index, then value
print(nums)
# [1, 99, 2, 3, 5, 6]


# remove() – remove by value
nums.remove(99)
print(nums)
# [1, 2, 3, 5, 6]
# Error if value not found

# In this case, both points to the same reference
# tea_varities_copy = tea_varities

# In this case, copy of the list is passed
tea_varities_copy = tea_varities.copy()
tea_varities_copy.append("Lemon")
print(tea_varities_copy)
print(tea_varities)


squared_num = [x**2 for x in range(10)]
print(squared_num)

cube_num = [y**3 for y in range(10)]
print(cube_num)

