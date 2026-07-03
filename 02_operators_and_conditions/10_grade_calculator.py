# Question 10
# calculate the grade
marks = float(input("Enter you marks(0-100):"))
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks <= 90:
    print("Grade: B")
elif marks >= 70 and marks <= 80:
    print("Grade: C")
elif marks >= 60 and marks <= 70:
    print("Grade: D")    
elif marks >= 50 and marks <= 60:
    print("Grade: E")
elif marks >= 40 and marks <= 50:
    print("Grade: F")
elif marks >= 30 and marks <= 40:
    print("Grade: G")
else:
    print("fail")        

