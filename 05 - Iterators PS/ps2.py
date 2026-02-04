# Calculate the sum of even numbers upto a given number n.

number = int(input("Enter the number of upto which you want the sum of even numbers: "))
even_sum = 0
for n in range(0, number + 1):
    if n % 2 == 0:
        even_sum += n
print(f"Even sum = {even_sum}")
