#Questio 2.
#Write a function to add two numbers.

#Method 1.
''' def add(a, b):
    return a + b
ans = add(5, 3)
print(ans)  '''

#Method 2.
'''def add(a, b):
    print("Sum =", a + b)

add(10, 20)'''

#Method 3.
def add(a, b):          # defines a function named add and a, b arfe function parameters
    return a + b         #return the sum of two nos
num1 = int(input("Enter first number:"))       
num2 = int(input("Enter second number:"))
result = (num1 + num2)       # calls the function and store the returns value
print("Sum=", result)        #displays the sum
