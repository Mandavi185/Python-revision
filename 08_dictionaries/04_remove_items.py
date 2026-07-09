#Question 4
# Remove an item using pop() and del
# method1. Using pop()
'''
student = {
    "name": "Mandavi",
    "age": 20,
    "branch": "CSE"
}

student.pop("age")

print(student)
'''
#method2. Using del
student = {
    "name": "Mandavi",
    "age": 20,
    "branch": "CSE"
}

del student["branch"]

print(student)