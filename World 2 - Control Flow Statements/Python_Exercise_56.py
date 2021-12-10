#Python Exercise 56

"""
Develop a program that reads the name, age and gender of 4 people and shows:
- The average age of the group.
- What's the older man's name.
- How many women are under 20 years old.
"""
ages = []
man_ages = []
women_under_20 = 0
older_man = ''
for c in range (1, 5):
    print(f'{c}° Person')
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender:[M/F] ')).upper().strip()
    ages.append(age)
    if gender == 'F' and age <= 20:
        women_under_20 += 1
    elif gender == 'M':
        man_ages.append(age)
        if max(man_ages) == age:
            older_man = name
    else:
        print('[ERROR]')
average = sum(ages) / len(ages)
print(f'The average age is {average}')
if sum(man_ages) > 0:
    print(f'The older man is {older_man} with {max(man_ages)} years old')
if women_under_20 == 1:
    print(f'There is one woman under 20 years old.')
elif women_under_20 >= 1:
    print(f'There are {women_under_20} women under 20 years old')
else:
    print(f'There are no women under 20 years old.')
