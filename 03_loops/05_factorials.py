#Question 5.
# Factorials
# 1st way
''' n = int(input("Enter the value of n:"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Factorial=", fact) '''

# 2nd way
n = int(input("Enter a number:"))
fact = 1
i = 1
while (i <= n):
    fact = fact * i
    i += 1
print("Factorial=", fact)    
