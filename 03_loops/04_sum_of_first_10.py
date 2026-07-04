#Question 5.
# Sum of first 10 natural numbers.

# 1st way
'''n = int(input("Enter the value of n:"))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum = ", sum)  '''

#2nd way
n = int(input("Enter the value of n:"))
sum = 0
i = 1
while (i <= n):
    sum = sum + i
    i += 1
print("Sum =", sum)


