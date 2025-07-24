#square each number in a list
numbers = [1, 2, 3, 4, 5]

def square(num):
    return num * num

squared_numbers = map(square, numbers)
print(list(squared_numbers))

#with multiple iterables - add elements from each list
list_item1 = [4, 6, 7, 3, 2]
list_item2 = [3, 5, 9, 1, 4]

added_list_items = map(lambda x, y : x + y, list_item1, list_item2)
print(list(added_list_items))

#Apply 10% discount to each price and get new list of discounted prices
prices = [150, 200, 100, 80, 60]

def discount(price):
    return price - (price * 0.1)

calculated_price = map(discount, prices)
print(list(calculated_price))   

