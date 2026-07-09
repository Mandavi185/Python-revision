#Question 8.
# Create a student record dictionary and display all details

student = {
    "roll": 101,
    "name": "Mandavi",
    "age": 20,
    "branch": "CSE",
    "city": "Kolkata"
}

for key, value in student.items():
    print(key, ":", value)