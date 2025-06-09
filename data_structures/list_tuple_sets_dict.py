#data_structures
#lists
friends = [["Ana", 10], ["Barbie", 20], ["charlie", 30]]
print(friends[0] [1]) #10
print(friends[0] [0]) #Ana

#tuple
school = "classA",
print(school)
classes = ("secA", "secB", "secC")
print(classes)
all_classes = classes + ("secD",)
print(all_classes) #can't modify the existing tuple. It creates a new tuple

currencies = 0.8, 1.2 #tuple
usd, euro = currencies
print(usd)
print(euro)

#sets
science_students = {"Anu", "Bhanu", "Chandu"}
arts_students = {"Bhanu", "Dhanu", "Geetha"}
science_but_not_arts = science_students.difference(arts_students)
arts_but_not_science = arts_students.difference(science_students)
print(science_but_not_arts)
print(arts_but_not_science)
not_in_both = science_students.symmetric_difference(arts_students)
in_both = science_students.intersection(arts_students)
all_students = science_students.union(arts_students)
print(not_in_both)
print(in_both)
print(all_students)

#dictionary
dict_example = {"Nicky":20, "pinky":30, "meena":40}
print(dict_example["Nicky"])
dict_example["reena"] = 50
print(dict_example)
student_details = (
    {"name":"bhagya", "marks":85},
    {"name":"pushya", "marks":95},
    {"name":"bhavya", "marks":75}

)
print(student_details[0]["name"])
