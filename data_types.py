#data_types_int_and_float

#integer data type
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
sum_of_nums = first_num + second_num
print(f"The sum of {first_num} and {second_num} is {sum_of_nums}")
#integer division
num_int = 13
int_div = num_int // 2
print (f"The result of interger division is {int_div}")


#float data type
PI = 3.14 #define variable in uppercase to signify that it is a constant
radius = float(input("Enter the radius of the circle: "))
circle_area = PI * radius ** 2
print(f"The area of the circle with radius {radius} is {circle_area}")
#float division
float_div = 13 / 2
print(f"The result of float division is {float_div}")
#mod operation
remainder = 13 % 2
print(f"The remainder of the division in {remainder}")


#data_types_strings

str_with_single_quotes = "Hello!, It's me, Geethanjali."
str_with_double_quotes = 'He told, "Its an amazing place to be visited".'
str_with_escape_character = 'She told, \'Weather is good today\'.' #escaping
#multiline strings - can be used for commenting
multiline_string = """Hello!,

It's a multiline string.

"""
print(str_with_single_quotes)
print(str_with_double_quotes)
print(str_with_escape_character)
print(multiline_string)

#string formatting
#concatenation of strings
emp1_name = "Pooja"
emp1_greeting = "Good morning, "+ emp1_name
print(emp1_greeting)

emp1_age = 24
emp1_details = f"Employee age is {emp1_age}" #f string
print(emp1_details)

#example2
emp2_name = "Kavya"
emp2_greeting = f"Good morning, {emp2_name}"
print(emp2_greeting)
emp2_name = "Kavya keerthi"
print(emp2_greeting) #emp name is not getting changed

#example3
emp3_name = "Jose"
emp3_greeting = "Good morning, {}"
print(emp3_greeting.format(emp3_name))
emp3_name = "Ram"
print(emp3_greeting.format(emp3_name))

#example4
emp4_name = "Megha"
emp4_greeting = "Good morning, {emp_name}"
print(emp4_greeting.format(emp_name = emp4_name))


#data_type_boolean
print(bool(0)) #false
print(bool(15)) #true
print(bool("")) #empty string is false
print(bool("Hello")) #non-empty string is true
print(bool([])) #empty list is false
print(bool([1, 2, 3])) #non-empty list is true

#boolean operations
min_age = 18
your_age = int(input('Enter your age'))
under_age = your_age < min_age
print(under_age)
over_age = your_age >= min_age
print(over_age)
age_matches = min_age == your_age
print(age_matches)

#OR operation
default_greeting = "there"
name_data = input('enter username: optional')
username = name_data or default_greeting
print(f"Hallo, {username}")

#AND operation
percentage = int(input("Enter your percentage:"))
distinction = percentage >= 85 and percentage <=100
first_class = percentage >= 60 and percentage < 85
second_class = percentage >= 35 and percentage < 60
print(f"Distinction: {distinction}, First Class: {first_class}, Second Class: {second_class}")


#data_structures
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
print(all_classes) #can't modify the existing tuple. It creates a new tuple

currencies = 0.8, 1.2 #tuple
usd, euro = currencies
print(usd)
print(euro)

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
