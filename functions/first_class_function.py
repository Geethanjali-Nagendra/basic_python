def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")   

number = int(input("Enter a number: "))

even_number = is_even
even_number(number)  # calling the function using the variable that holds the function reference

#example 
total_score = lambda sequence: sum(sequence)
highest_score = lambda sequence: max(sequence)

students = [
    {"name":"Anu", "score":(85, 90, 95)},
    {"name":"Balu", "score":(75, 80, 85)},
    {"name":"Chitra", "score":(95, 100, 90)},
    {"name":"Dinesh", "score":(65, 70, 75)}
]

operation = input("Enter total_score or highest_score:")

for student in students:
    name = student["name"]
    score = student["score"]

    print(f"student name: {name}")

    if operation == "total_score":
        print(f"Total score: {total_score(score)}")
    elif operation == "highest_score":
        print(f"Highest score: {highest_score(score)}") 
    else:
        print("Invalid operation")
