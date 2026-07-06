# Question 12
# Remove Duplicates from a List

numbers = [10, 20, 20, 30, 40, 40, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)