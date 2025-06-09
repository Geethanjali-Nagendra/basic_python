#conditional_statements

#if elif and else
friends = ["Ammu", "Bhavi", "deepa"]
family = ["Pooja", "lekha", "smitha"]

member = input("enter the members name:")

if member in friends:
    print(f'Hello, {member}')
elif member in family:
    print(f'Hello, {member}')
else:
    print('we dont know you')

#Loops
#while loop
user_input = input('Do you wish to run the program (Yes/No):')

while user_input == "Yes":
    print('we are running a program')
    user_input = input('Do you still wish to run the program (Yes/No):')

print('program execution is stopped')

#exercise1
user_option = input('Choose the option p or q')

while user_option != 'q':
    if user_option == 'p':
        print("Hello")
    user_option = input('choose the option p or q')

#for loop

for i in range(5):
    print(i)
for j in range(1,10):
    print(j)
for k in range(2,20,3):
    print(k)

#exercise1

students = [
    {"name":"merry", "grade":86},
    {"name":"cherry","grade":90},
    {"name":"sannu", "grade":70}
]
for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has grade of {grade}")

#exercise2 break keyword
# Guessing game
secret_number = 8
while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number.")
        break
    else:
        print("Try again!")


#exercise3 continue keyword
#skip city names starts with 'C'
city_names =["Delhi", "Chennai", "Mumbai", "Chandigarh", "Bangalore", "Mysuru"]
for city in city_names:
    if city.startswith("C"):
        continue
    print(city)

