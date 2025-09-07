class Employee:

    company = "IT solutions"
    hike_percentage = 0.05
    
    def __init__(self, emp_name, emp_id, emp_role, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_role = emp_role
        self.emp_salary = emp_salary

    def employee_info(self):
        print(f"Employee Name : {self.emp_name}")
        print(f"Employee ID : {self.emp_id}")
        print(f"Employee Role : {self.emp_role}")    
        
    @classmethod
    def update_hike_percentage(cls, new_hike_percentage):
        cls.hike_percentage = new_hike_percentage
        print(f"Revised hike percentage for current financial year: {cls.hike_percentage * 100}%")

    def apply_hike(self):
        self.emp_salary += self.emp_salary * Employee.hike_percentage
        print(f"New salary after hike: {self.emp_salary}")

    @staticmethod
    def emp_grade(years_of_experience):
        if years_of_experience < 2:
            print("Junior")
        elif 2 <= years_of_experience <5:
            print("Mid-level")
        else:
            print("Senior")

print(f"Company : {Employee.company}")
Employee.update_hike_percentage(0.1)

emp1 = Employee("Shilpa", 12345, "developer",80000)
emp1.employee_info()
emp1.apply_hike()
Employee.emp_grade(10)

emp2 = Employee("Rahul", 67856, "tester",60000)
emp2.employee_info()
emp2.apply_hike()
Employee.emp_grade(4)

emp3 = Employee("Megha", 17089, "support", 50000)
emp3.employee_info()
emp3.apply_hike()
Employee.emp_grade(1)
