#returns an iterable of tuples with index and value
months = ["January", "February", "March", "April", "May"]

for counter, month in enumerate(months):
    print(counter)
    print(month)
    
print(list(enumerate(months, start=1)))  # starts counting from 1
print(dict(enumerate(months)))
