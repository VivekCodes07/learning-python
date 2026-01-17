# nested loop = A loop within another loop (outer, inner)

# outer loop:
#   inner loop:


for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")
    print() # This will just print a new line


rows = 5
# In the first iteration i is 0.
for i in range(rows):
    # Inner loop prints stars based on the current row number (i)
    for j in range(i + 1):
        print("*", end=" ")
    print() # Moves to the next line
