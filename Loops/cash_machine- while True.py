correct_pin=1234
correct_amounts={50,100,150,200}

pin_attempts_left=3
amount_attempts_left=3


while True:

    pin=int(input('Enter your pin: '))  # ask user for PIN number
    
    if pin==correct_pin:
        print('Correct PIN')   # if PIN is correct
        
        amount=int(input('Please, select the amount: (50,100,150,200):'))   # ask for amount to withdraw
        
        if amount in correct_amounts:  # if amount is correct
            print('Please collect the money')
            print('Thank you for using our services. Have a nice day:)')
            break
            
        else:  # wrong amount selected
            
            amount_attempts_left-=1    # reduce attempt count
            
            if amount_attempts_left > 0:
                print('Sorry, the selected amount is incorrect. Please select correct amount:')
                print(f'You can try {amount_attempts_left} times')
            else:
                print('Sorry, too many wrong attempts. Try another time!')
                break
    else:
        
        # exit option - user can enter 0 instead of PIN
        
        if pin == 0:
            print('Operation canceled. Goodbye!')
            break
        
        pin_attempts_left-=1  # wrong PIN - reduce attempts
        
        if pin_attempts_left > 0:
            print('Wrong pin! Please try again.')
            print(f'You can try {pin_attempts_left} more times')
                 
        else:
            print('Too many wrong attempts! Card blocked!')  # no attempts left - card blocked
            break
    
    
#Example run:

#Enter your pin: 2548
#Wrong pin! Please try again.
#You can try 2 more times
#Enter your pin: 21455
#Wrong pin! Please try again.
#You can try 1 more times
#Enter your pin: 0
#Operation canceled. Goodbye!