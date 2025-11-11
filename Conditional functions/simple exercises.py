#SIMPLE CONDITIONAL INSTRUCTIONS

#1) Greeting after entering your name.

name=input('What is your name?') #ask for name

if name == 'Ola':  #condition 1
    print('Hi Ola, nice to meet you!')  #returns
    
elif name == 'Frank':  # condition 2
    print('Hello Frank! How are you?')  #returns
    
else:   
    print(f'Hi {name}!')  #if the condition is not met


#2) Age check.

age=int(input('Enter your age: '))

if age< 15:         # if less than 15
    print('You are a child')
    print(f'To be an adult you need {18-age}years')
    
elif age< 18:       # if less than 18
    print('You are underage')
    print(f'To be an adult you need {18-age}')
    
elif age == 18:     # if 18
    print('You are 18 years old')
    
elif age <= 60:    #less than or equal to 60
    print('You are an adult')
    
else:
    print('You are older')