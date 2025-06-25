batch1_students = ["sonia", "merry", "john", "paul"]

student_name = input("Enter the name of the student: ")

if not student_name in batch1_students:
    print("You are not the student of batch 1")
else:
    print("You are the student of batch 1")

