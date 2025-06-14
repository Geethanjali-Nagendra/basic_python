#conditional_statements

#if elif and else
friends = ["Ammu", "Bhavi", "deepa"]
family = ["Pooja", "lekha", "smitha"]

member = input("enter the members name:")

if member in friends:
    print(f'Hello, friend: {member}')
elif member in family:
    print(f'Hello, family: {member}')
else:
    print('we dont know you')
