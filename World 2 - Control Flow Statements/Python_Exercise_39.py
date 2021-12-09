#Pyhton Exercise 39

#Make a program that reads person's year of birth and reports, according to their age:
# If he's still going to enlist in military service.
# If he's past enlistment time.
from datatime import date
print('Military Enlistment informator!')
birth = int(input('Enter your birth year:'))
year = date.today().year
age = year - birth
print(f'Whoever was born in {birth} have {age} in {year}.')
if age < 18:
    print(f'Still {18-age} years to enlist')
elif age > 18:
    print(f'Your enlistment was in {birth+18}.')
else:
    print('Your enlistment will be this year.')
