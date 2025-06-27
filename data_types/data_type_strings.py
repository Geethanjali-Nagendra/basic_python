str_with_single_quotes = "Hello!, It's me, Geethanjali."
str_with_double_quotes = 'He told, "Its an amazing place to visit".'
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
