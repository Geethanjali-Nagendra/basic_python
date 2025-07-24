difference = lambda operand1, operand2 : operand1 - operand2
print(difference(10, 6))

print((lambda operand3, operand4 : operand3 * operand4) (5, 6))

#calculate average score of students
average_score = lambda sequence : sum(sequence) / len(sequence)

students = [
    {"name":"Anu", "score":(85, 90, 95)},
    {"name":"Balu", "score":(75, 80, 85)},
    {"name":"Chitra", "score":(95, 100, 90)},
    {"name":"Dinesh", "score":(65, 70, 75)}
]

for student in students:
    print(average_score(student["score"]))
