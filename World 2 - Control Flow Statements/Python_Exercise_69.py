#Python Exercise 69

"""
Create a program that reads the age and gender of different people. For each registered person, the program must ask whether the user wants to continue or not.
No end, show how many:
a) people of legal age.
b) men were registered.
c) women under 20 years of age.
"""
adults = men = women = 0
while True:
    age = int(input('Enter the age:\n'))
    gender = ' '
    while gender not in 'MF':
        gender = input('Enter the gender: [M/F]\n').strip().upper()[0]
    if age >= 21:
        adults += 1
    if gender == 'M':
        men += 1
    if gender == 'F':
        if age <= 20:
            women += 1
    contin = ' '
    while contin not in 'YN':
        contin = input('Want to continue? [Y/N] ').strip().upper()[0]
    if contin == 'N':
        break
print(f'{adults} registered adults.')
print(f'{men} men were registered.')
print(f'{women} registered women under 20 years of age')
