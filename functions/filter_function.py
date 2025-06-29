#filter the country names that start with 'I'
countries = ["Australia", "Brazil", "Canada", "India", "Japan", "Indonesia", "Hungary", "Italy", "Germany"]

def country_names_starts_with_i(country):
    return country.startswith("I")

country_names = filter(country_names_starts_with_i, countries)
print(list(country_names))

#filter numbers greater than the average
numbers = [82, 84, 85, 87, 88, 90, 94, 96, 98, 100]

average = sum(numbers) / len(numbers)
print(f"Average: {average}")

numbers_greater_than_average = filter(lambda num : num > average, numbers)
print(tuple(numbers_greater_than_average))
