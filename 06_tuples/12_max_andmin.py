#Question 12.
# Maximum and Minimum Element in a Tuple.
#Method 1.
'''
numbers = (10, 50, 20, 80, 30)

print("Maximum =", max(numbers))
print("Minimum =", min(numbers))
'''

#Method 2.
# Without using max() and min()

numbers = (10, 50, 20, 80, 30)

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum =", maximum)
print("Minimum =", minimum)