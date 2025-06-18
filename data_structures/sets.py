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
