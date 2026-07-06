#Question 9.
# Count the even numbers in a list.

numbers = [10, 15, 8, 23, 6, 12, 7]

count = 0

for num in numbers:
    if num % 2 == 0:
        count = count + 1

print("Even numbers =", count)