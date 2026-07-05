#Question 4.
#Write a function to find the factorial of a number.

def factorial(n):                #defines the function named factorial
    fact = 1                     # intializes the factorial
    for i in range(1, n+1):       # loops from 1 to n  
        fact = fact * i            # Multiplies each number
    return fact                      # Returns the factorial
n = int(input("Enter a number:"))
print("Factorial=", factorial(n))     # factorial(n) = calls the function