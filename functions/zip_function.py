colleagues = ["Shashi", "Sowmya", "Sanjana", "Suman"]
time_since_joined = [10, 6, 4, 3]

more_than_five_yoe = {
    colleagues[i] : time_since_joined[i]
    for i in range(len(colleagues))
    if time_since_joined[i] > 5
}
print(more_than_five_yoe)

#zip function to combine 2 or more lists into a single iterable of tuples
colleagues_with_yoe = dict(zip(colleagues, time_since_joined))
print(colleagues_with_yoe)

colleagues_with_yoe_role = list(zip(colleagues, time_since_joined, ["HR", "Finance", "IT", "Admin"]))
print(colleagues_with_yoe_role)
