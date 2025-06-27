print(bool(0)) #false
print(bool(15)) #true
print(bool("")) #empty string is false
print(bool("Hello")) #non-empty string is true
print(bool([])) #empty list is false
print(bool([1, 2, 3])) #non-empty list is true

min_age = 18
your_age = int(input('Enter your age'))

under_age = your_age < min_age
print(under_age)

over_age = your_age >= min_age
print(over_age)

age_matches = min_age == your_age
print(age_matches)
