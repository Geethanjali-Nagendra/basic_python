#strings
str1 = "Hello, it's me"
str2 = 'he told, "its an amazing place to be visited".'
str4 = 'he told, \'its an amazing place to be visited\'.' #escaping
#multiline strings
str3 = """hello,

It's a multiline string.

"""
print(str1)
print(str2)
print(str3)
print(str4)

#integer division and float division
int_div = 13 // 2
print (int_div)
float_div = 13 / 2
print(float_div)
remainder = 13 % 2
print(remainder)

#string formatting
#example1
emp1_name = "Pooja"
emp1_greeting = "Good morning "+ emp1_name
print(emp1_greeting)

emp1_age = 24
emp1_details = f"Employee age is {emp1_age}" #f string
print(emp1_details)

#example2
emp2_name = "Kavya"
emp2_greeting = f"Good morning {emp2_name}"
print(emp2_greeting)
emp2_name = "Kavya keerthi"
print(emp2_greeting) #emp name is not getting changed

#example3
emp3_name = "Jose"
emp3_greeting = "Good morning {}"
print(emp3_greeting.format(emp3_name))
emp3_name = "Ram"
print(emp3_greeting.format(emp3_name))

#example4
emp4_name = "Megha"
emp4_greeting = "Good morning {emp_name}"
print(emp4_greeting.format(emp_name = emp4_name))

#input function 
deine_name = input('Wie heißt du?')
meine_name = "Geethanjali"
print(f"Hallo {deine_name}, Ich bin {meine_name}")

age = int(input("enter your age"))
print(f'you have lived for {age*12} months')

#boolean comparasions
min_age = 18
your_age = int(input('Enter your age'))
under_age = your_age < min_age
print(under_age)
over_age = your_age >= min_age
print(over_age)
age_matches = min_age == your_age
print(age_matches)

default_greeting = "there"
name_data = input('enter username: optional')
username = name_data or default_greeting
print(f"Hallo, {username}")

#lists
friends = [["Ana", 10], ["Barbie", 20], ["charlie", 30]]
print(friends[0] [1]) #10
print(friends[0] [0]) #Ana

#tuple
school = "classA",
print(school)
classes = ("secA", "secB", "secC")
print(classes)
all_classes = classes + ("secD",)
print(all_classes)

#sets
science_students = {"Anu", "Bhanu", "Chandu"}
arts_students = {"Bhanu", "Dhanu", "Geetha"}
science_but_not_arts = science_students.difference(arts_students)
arts_but_not_science = arts_students.difference(science_students)
print(science_but_not_arts)
print(arts_but_not_science)
not_in_both = science_students.symmetric_difference(arts_students)
in_both = science_students.intersection(arts_students)
all_students = science_students.union(arts_students)
print(not_in_both)
print(in_both)
print(all_students)

#dictionary

dict_example = {"Nicky":20, "pinky":30, "meena":40}
print(dict_example["Nicky"])
dict_example["reena"] = 50
print(dict_example)
student_details = (
    {"name":"bhagya", "marks":85},
    {"name":"pushya", "marks":95},
    {"name":"bhavya", "marks":75}

)
print(student_details[0]["name"])













