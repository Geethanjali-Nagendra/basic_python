def even():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")   

even_number = even
even_number()  # calling the function using the variable that holds the function reference

#example 
operations_function = {
    "total_score": lambda sequence: sum(sequence),
    "highest_score": lambda sequence: max(sequence)
}

students = [
    {"name":"Anu", "score":(85, 90, 95)},
    {"name":"Balu", "score":(75, 80, 85)},
    {"name":"Chitra", "score":(95, 100, 90)},
    {"name":"Dinesh", "score":(65, 70, 75)}
]

for student in students:
    name = student["name"]
    score = student["score"]

    print(f"student name: {name}")
    operation = input("Enter total_score or highest_score:")

    result = operations_function[operation]  # calling the function using the variable that holds the function reference
    print(result(score))
