#if and else 

friends = ["Ammu", "Bhavi", "deepa"]
family = ["Pooja", "lekha", "smitha"]

member = input("enter the members name:")

if member in friends:
    print(f'Hello, {member}')
elif member in family:
    print(f'Hello, {member}')
else:
    print('we dont know you')

#while loop

user_input = input('Do you wish to run the program (Yes/No):')

while user_input == "Yes":
    print('we are running a program')
    user_input = input('Do you still wish to run the program (Yes/No):')

print('program execution is stopped')

#exercise
user_option = input('Choose the option p or q')

while user_option != 'q':
    if user_option == 'p':
        print("Hello")
    user_option = input('choose the option p or q')

#for loop
for i in range(2,20,3):
    print(i)

students = [
    {"name":"merry", "grade":86},
    {"name":"cherry","grade":90},
    {"name":"sannu", "grade":70}
]
for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has grade of {grade}")


currencies = 0.8, 1.2 #tuple
usd, euro = currencies
print(usd)
print(euro)












