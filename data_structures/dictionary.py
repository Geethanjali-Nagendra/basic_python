dict_example = {"Nicky":20, "Pinky":30, "Meena":40}
print(dict_example["Nicky"])
dict_example["Reena"] = 50
print(dict_example)

student_details = (
    {"name":"Bhagya", "marks":85},
    {"name":"Pushya", "marks":95},
    {"name":"Bhavya", "marks":75}

)
print(student_details[0]["name"])

#iterating through a dictionary and printing the keys
months = {
    "January":31,
    "February":28,
    "April":30
}

for month in months:
    print(f"Month: {month}")

#iterating through a dictionary and printing the values
for days in months.values():
    print(f"Days: {days}")

#iterating through a dictionary and printing the key-value pairs
for month, days in months.items():
    print(f"{month} has {days} days")

#finding a key in a dicytionary
for month in months:
    if month == "February":
        print(f"{month} is found in the dictionary")
        break
else:
    print("February is not found in the dictionary")    
