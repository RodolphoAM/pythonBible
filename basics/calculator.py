operation = input('Please type in the operation:\n'
                  '+ for addition\n'
                  '- for subtraction\n'
                  '* for multiplication\n'
                  '/ for division\n')
number_1 = int(input('Enter your first number\n'))
number_2 = int(input('Enter your second number\n'))

# Addition
if operation == '+':
    print('{}+{}'.format(number_1, number_2))
    print(number_1+number_2)

# Subtraction
elif operation == '-':
    print('{}-{}'.format(number_1, number_2))
    print(number_1-number_2)

# Multiplication
elif operation == '*':
    print('{}*{}'.format(number_1, number_2))
    print(number_1*number_2)

# Division
elif operation == '/':
    print('{}/{}'.format(number_1, number_2))
    print(number_1/number_2)

else:
    print('You selected an invalid operation')