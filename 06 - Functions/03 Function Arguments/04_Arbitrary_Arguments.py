def average(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(f"The average is: {sum / len(numbers)}")

average(5, 5, 5)