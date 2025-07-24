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

#else keyword with for loop - check if a number is prime number
input_num = int(input("Enter the number:"))

for n in range(2,input_num):
    if input_num % n == 0:
        print(f"{input_num} is not a prime number")
        break
else:
    print(f"{input_num} is a prime number")
