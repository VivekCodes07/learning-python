'''
Sets - Mutable
     - Duplicate Values -> Not allowed
     - Every element is unique
     - Unordered -> Cannot access them through index values.
     - Heterogeneous - Set is semi-heterogeneous it can store some data types like 
       string, numbers, tuples but not everything
'''
list1 = [23, 67, 45, 67] # Orderd and Duplicate Values allowed
print(f"List: {list1}")

set1 = {23, 67, 45, 34, 67} # Unordered and Duplucate Values not allowed
print(f"Set: {set1}") 

set2 = {20, "Vivek", "Google", 90000.0}
print(f"Set2: {set2}")
print(type(set2))


# Set Methods:

set4 = {1, 2, 3, 4, 5}
set4.add(7)
set4.remove(5) 
print(set4)

set4.clear()
print(set4)


A = {1, 2, 3, 4}
B = {3, 4, 5}

union_set = A.union(B) 
print(f"Union of Set A and Set B: {union_set}")

intersection_set = A.intersection(B)
print(f"Intersection of Set A and Set B: {intersection_set}")

difference_set = A.difference(B)
print(f"Difference Set: {difference_set}")

symmetric_diff = A.symmetric_difference(B)
print(f"Symmetric Difference: {symmetric_diff}")

'''
print(A | B) # Union
print(A & B) # Intersection
print(A - B) # Difference
print(A ^ B) # Symmetric Difference
'''