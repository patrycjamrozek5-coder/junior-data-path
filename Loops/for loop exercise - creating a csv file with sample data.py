import pandas as pd 
import random
 
random.seed(42)

names=['Violet', 'Carol', 'Simon', 'Elisabeth', 'Lila','Thomas', 'Sophia', 'Paul', 'Eva', 'Olivia', 'Amelia', 'Matthiew']
cities=['Warsaw', 'Lisbon', 'Osaka', 'Mumbai', 'Houston', 'Seattle', 'Gdańsk','Indianapolis','Chorzów', 'Katowice','San Diego', 'Wrocław']

n=1000 #number of records

data={
    
    'name': [random.choice(names) for _ in range(n)],         # column name - draws name from the list of names
    'city': [random.choice(cities) for _ in range (n)],        # column city - draws city from the list of cities
    'income': [random.randint(5000, 35000) for _ in range(n)],  # column income - draws numbers from a specific range
    
    # empty columns completed with a loop
    
    'has_children': [],
    'number_of_children': [],
    'has_pet': [], 
    'pet_type': []+
}

# a loop that adds values to the children and pets columns

for _ in range(n):  
    
    if random.choice([True, False]):        # randomly decides whether to have a children 
        data['has_children'].append('yes')
        data['number_of_children'].append(random.randint(1, 5))    # draws number of children from 1 to 5
    
    else:
        data['has_children'].append('no')   # if there are no children - enter no
        data['number_of_children'].append(0)   # enter 0
    
    # randomly assigned pets
    
    if random.choice([True, False]):
        data['has_pet'].append('yes')
        data['pet_type'].append(random.choice(['dog', 'cat', 'hamster', 'bird', 'rabbit']))
    else:
        data['has_pet'].append('no')
        data['pet_type'].append('no pet')    # if doesn't have a pet - no pet

df=pd.DataFrame(data)

df.to_csv('data_people.csv', index=False, encoding='utf-8-sig')
print('file saved to data_people.csv')|