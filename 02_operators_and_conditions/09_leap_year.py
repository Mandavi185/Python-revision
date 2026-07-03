# Question 9
# check whwther a year is leapyear

num = int(input("Enter a number:"))
if (num % 4 == 0 and num % 100 != 0 or num % 400 ==0):
    print("Leapyear")
else: 
    print("not a leap year")