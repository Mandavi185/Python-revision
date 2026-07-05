#Question 1.
#Write a function to find the square of a number.
# 1st way
'''def square(a):
    print("Square=", a*a)
square(5)   '''

#2nd way
def square(n):
    return n*n
num = int(input("Enter a number:"))
result = square(num)
print("Square =", result )
