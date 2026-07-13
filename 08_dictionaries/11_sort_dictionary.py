# Question 11
# sort dictionary

student = {
    "name": "Mandavi",
    "age": 20,
    "branch": "CSE",
    "city": "Kolkata"
}

for key in sorted(student):
    print(key, ":", student[key])