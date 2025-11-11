import random

the_number = random.randint(1, 100)  #the computer randomly selects a number from 1 to 100

while True:
    attempt = int(input('Enter a number between 1 and 100: '))
    
    if attempt < the_number:   #if the number is smaller
        print('Your guess is too low, try again')
    
    elif attempt > the_number:  #if the number is bigger
        print('Your guess is too high, try again')
    
    else:
        print('Congratulations! You guessed the selected number!')
        break  #stops the loop



#Example run:
#Enter a number between 1 and 100: 50
#This number is smaller than the selected one, try again
#Enter a number between 1 and 100: 70
#This number is smaller than the selected one, try again
#Enter a number between 1 and 100: 80
#Congratulations! You guessed the selected number!