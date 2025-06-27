number = int(input("Enter a two-digit number: "))

if number < 10 or number > 99:
    print("Please enter a valid two-digit number.")


letter = input("Enter a letter: ")
if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("It's a vowel")
else:
    print("It's a consonant")
    
friends = ["Ammu", "Bhavi", "Deepa"]
family = ["Pooja", "Lekha", "Smitha"]
member = input("Enter the member's name:")
if member in friends:
    print(f'Hello, friend: {member}')
elif member in family:
    print(f'Hello, family: {member}')
else:
    print('We don\'t know you')
