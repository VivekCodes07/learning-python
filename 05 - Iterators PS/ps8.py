# Check if a number is prime.

number = int(input("Enter a number to check if it is prime or not: "))

if number <= 1:
    print("It is not a Prime number")
else:
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break

    if is_prime:
        print("Yes, it is a Prime number")
    else:
        print("It is not Prime")
