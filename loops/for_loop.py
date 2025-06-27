for i in range(5):
    print(i)
for j in range(1,10):
    print(j)
for k in range(2,20,3):
    print(k)

# Looping through a list of dictionaries
students = [
    {"name":"merry", "grade":86},
    {"name":"cherry","grade":90},
    {"name":"sannu", "grade":70}
]
for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has grade of {grade}")
