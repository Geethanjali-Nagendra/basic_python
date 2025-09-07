class Student:
    School_name = "BGS High School"

    def __init__(self, name, class_name, marks):
        self.name = name
        self.class_name = class_name
        self.marks = marks

    def student_info(self):
        print(f"Student Name : {self.name}")
        print(f"Class Name : {self.class_name}")
        print(f"Marks : {self.marks}")
        print(f"School Name : {Student.School_name}")

student_1 = Student("Anagha", "10th", 86)
student_1.student_info()

student_2 = Student("Bhanu", "10th", 78)
student_2.student_info()
