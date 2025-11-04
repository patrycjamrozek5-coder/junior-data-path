# Discount in the store - conditional functions

discount=0
price=100
status='student', 'senior'
status=input('Enter your status: ("senior", "student"):')


if status =='student':
    student_ID = input('Please show your student ID. Pres yes or no: ')
    if student_ID =='yes':
        discount = price * 0.20
    elif student_ID == 'no':
        print('Sorry, you need your student ID to get the discount.')
        discount = price
    else:
        print('Error: wrong status!')
        print('Try again')
        exit()
elif status=='senior':
    age = int(input('Please specify age: '))
    if age <= 65:
        discount = price * 0.10
    else:
        discount = price * 0.30
elif status!='student''senior':
    print('Error: wrong status!')
    print('Try again.')
    exit()
else:
    discount = price * 0.10
print(f'This is your actual price: {discount} zł')

#Example run:
#Enter your status: ("senior", "student"):student
#Please show your student ID. Pres yes or no: no
#Sorry, you need your student ID to get the discount.
#This is your actual price: 100 zł

#Enter your status: ("senior", "student"):fkfk
#Error: wrong status!
#Try again.