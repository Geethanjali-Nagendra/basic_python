#while loop
user_input = input('Do you wish to run the program (Yes/No):')

while user_input == "Yes":
    print('we are running a program')
    user_input = input('Do you still wish to run the program (Yes/No):')

print('program execution is stopped')

#exercise1
user_option = input('Choose the option p or q')

while user_option != 'q':
    if user_option == 'p':
        print("Hello")
    user_option = input('choose the option p or q')
