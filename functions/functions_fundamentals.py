def greetings(name): #defining a function
    print(f"Hallo {name}, Guten tag!")

name = input("Wie heißen Sie? ")
greetings(name) # calling the function


def add_numbers(a,b): # defining a function with parameters
    print(f"sum is {a+b}")

add_numbers(4,6) #6 and 4 are passed as arguments to the function add_numbers


def divide_numbers(x,y): #with return statement
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    else:
        return x / y
    
print(divide_numbers(10,5))
print(divide_numbers(5,0))


def multiply_numbers(u,v=4): # with default parameter
    return u * v

print(multiply_numbers(3)) # will use default value of v
print(multiply_numbers(7,5)) # will use provided value of v
print(multiply_numbers(2,v=6)) #named argument, v is set to 6

#note - if first parameter is default parameter then subsequent parameters must also be default parameters
#if first argument is named argument then all subsequent arguments must also be named arguments
