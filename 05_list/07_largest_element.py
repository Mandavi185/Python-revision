#Question 7.
# Find the largest element in a list.

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)