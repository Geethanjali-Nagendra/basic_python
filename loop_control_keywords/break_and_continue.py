#exercise1 break keyword
# Guessing game
secret_number = 8
while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number.")
        break
    else:
        print("Try again!")


#exercise2 continue keyword
#skip city names starts with 'C'
city_names =["Delhi", "Chennai", "Mumbai", "Chandigarh", "Bangalore", "Mysuru"]
for city in city_names:
    if city.startswith("C"):
        continue
    print(city)
