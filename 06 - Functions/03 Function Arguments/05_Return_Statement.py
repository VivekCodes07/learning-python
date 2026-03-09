# The return statement is used to return the value of the expression back to the calling function.

def average(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)

avg = average(4, 5, 6, 10)
print("The average is", avg)