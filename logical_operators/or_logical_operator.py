default_greeting = "there"
name_data = input('Enter the username: optional')

username = name_data or default_greeting
print(f"Hallo, {username}")
