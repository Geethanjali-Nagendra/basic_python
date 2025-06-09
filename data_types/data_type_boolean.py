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
