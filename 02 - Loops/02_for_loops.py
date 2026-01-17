# for loops = execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.

credit_card = "1234-7789-9876"

for x in credit_card:
    print(x)


for x in reversed(range(1, 11, 2)):
    print(x)
print("Happy New Year!")


for x in range(1, 16):
    if x == 5:
        continue
    else:
        print(x)