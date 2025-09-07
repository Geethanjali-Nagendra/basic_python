class Exam:

    sector = "Government"

    def __init__(self, name, registration_number, age, category):
        self.name = name
        self.registration_number = registration_number
        self.age = age
        self.category = category

    def age_eligibility(self):
        if self.age >= 18:
            print("Minimum age eligibility is 18 years")
        
    def no_of_attempts(self):
        print("Maximum number of attempts allowed is 3")

    def candidate_details(self):
        print(f"Candidate Name: {self.name}")
        print(f"Registration Number: {self.registration_number}")

class UPSC(Exam):

    def age_eligibility(self):
        if self.category == "General" and 22 <= self.age <= 30:
            print("Eligible for UPSC exam")
        elif self.category == "OBC" and 22 <= self.age <= 33:
            print("Eligible for UPSC exam")
        else:
            print("Age eligibility criteria not met for UPSC exam")

    def no_of_attempts(self):
        if self.category == "General":
            print("Maximum number of attempts allowed is 3")
        elif self.category == "OBC":
            print("Maximum number of attempts allowed is 6")

class Railways(Exam):

    def __init__(self, name, registration_number, age, category, location):
        super().__init__(name, registration_number, age, category)
        self.location = location    

    def age_eligibility(self):
        if self.category == "General" and 18 <= self.age <= 35:
            print("Eligible for Railways exam")
        elif self.category == "OBC" and 18 <= self.age <= 38:
            print("Eligible for Railways exam")
        else:
            print("Age eligibility criteria not met for Railways exam")

    def no_of_attempts(self):
        if self.category == "General":
            print("Maximum number of attempts allowed is 4")
        elif self.category == "OBC":
            print("Maximum number of attempts allowed is 7")

    def total_vacancies(self):
        if self.location == "South-west":
            print("Total vacancies available are 5000")
        elif self.location == "North-east":
            print("Total vacancies available are 3000")
        elif self.location == "Northern":
            print("Total vacancies available are 4000")

candidate1 = UPSC("Geetha", "UPSC1234", 28, "OBC")
candidate1.candidate_details()
candidate1.age_eligibility()
candidate1.no_of_attempts()

candidate2 = Railways("Arjun", "RRB5678", 34, "General", "South-west")
candidate2.candidate_details()
candidate2.age_eligibility()
candidate2.no_of_attempts()
candidate2.total_vacancies()
