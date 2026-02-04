# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter the number whose multiplication you want: "))

for n in range (1, 11):
    if n == 5:
        print("Skipped the fifth iteration")
        continue
    print(f"{number} X {n} = {number * n}")