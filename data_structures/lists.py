friends = [["Ana", 10], ["Barbie", 20], ["Charlie", 30]]
print(friends[0] [1]) #10
print(friends[0] [0]) #Ana

#iterating through a list of tuples
vegetables = [("carrot", 35), ("potato", 20), ("cucumber", 25), ("onion", 40)]

for vegetable, price in vegetables:
    print(f"Vegetable: {vegetable}, Price: {price}")

#list slicing
fruits = ["Apple", "Banana", "Grapes", "Papaya", "Mango"]

print(fruits[1:3]) #['Banana', 'Grapes']
print(fruits[1:]) #['Banana', 'Grapes', 'Papaya', 'Mango']
print(fruits[:3]) #['Apple', 'Banana', 'Grapes']
print(fruits[:]) # ['Apple', 'Banana', 'Grapes', 'Papaya', 'Mango'] creates a new list by copying the existing list
print(fruits[-3:]) #['Grapes', 'Papaya', 'Mango']
print(fruits[:-2]) #['Apple', 'Banana', 'Grapes']
print(fruits[-3:-1]) #['Grapes', 'Papaya']
print(fruits[-3:4]) #['Grapes', 'Papaya']

#list comprehension
list_of_numbers = [1,2,3,4,5]
doubled_numbers = []
for n in list_of_numbers:
    doubled_numbers.append(n*2)
print(doubled_numbers)

#we can write the above code in a single line using list comprehension
doubled_numbers_2 = [num*2 for num in list_of_numbers]
print(doubled_numbers_2)

#example1
fruits_lower_case = [fruit.lower() for fruit in fruits]
print(fruits_lower_case)

#comprehension with condition
odd_numbers = [odd for odd in list_of_numbers if odd % 2 == 1]
print(odd_numbers)
