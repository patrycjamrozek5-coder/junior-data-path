# Simple calculator - conditional functions

a=float(input('Enter your first number: '))
operation=input('Enter your operation: (+,-,*,/):)')
b=float(input('Enter your second number: '))

if operation =='+':
    result= a+b
    print(f'Result is {result}')
elif operation == '-':
    result= a-b
    print(f'Result is {result}')
elif operation == '*':
    result= a*b
    print(f'Result is {result}')
elif operation == '/':
    if b != 0:
        print('Error: division by zero is not allowed.')
    else:
        result = a/b
        print(f'Result is {result}')
else:
    print('Error: there are no such operations.')
    print('This is a simple calculator.')
    print('Please try again.')


#Example run:

#Enter your first number: -2
#Enter your operation: (+,-,*,/):)*
#Enter your second number: 5
#Result is -10.0

#Enter your first number: 5
#Enter your operation: (+,-,*,/):)^
#Enter your second number: 5
#Error: there are no such operations.
#This is a simple calculator.
#Please try again.