percentage = int(input("Enter your percentage:"))

distinction = percentage >= 85 and percentage <=100
first_class = percentage >= 60 and percentage < 85
second_class = percentage >= 35 and percentage < 60

print(f"Distinction: {distinction}, First Class: {first_class}, Second Class: {second_class}")
