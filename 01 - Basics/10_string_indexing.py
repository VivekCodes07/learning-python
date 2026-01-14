# indexing = accessing elements of a sequence using [] (indexing operator) [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0 : 4])


lang = "Python Programming"
print(lang[0:18:2])  # Pto rgamn
print(lang[::3])     # Ptnrrmn



text = "Python"

# Positive indexing
print(text[0])  # P
print(text[1])  # y
print(text[2])  # t

# Negative indexing
print(text[-1])  # n
print(text[-2])  # o

# Slicing (getting part of a string)
print(text[0:4])  # Pyth
print(text[2:])   # thon
print(text[:3])   # Pyt
