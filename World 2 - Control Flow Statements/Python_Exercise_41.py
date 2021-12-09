#Python Exercise 41
"""
The National Swimming Confederation needs a program that reads the year of birth
of an athlete and master of their category, according to age:
-up to 9 years old: MIRIM
-up to 14 years old: CHILDREN
-up to 19 years old: JUNIOR
-up to 25 years old: SENIOR
-above: MASTER
"""
from datetime import date

birth = int(input('Input the year the swimmer was born: '))
year = date.today().year
age = year - birth

if age <= 9:
    print(f'Classification: CHILD ATHLETE')
elif age <= 14:
    print(f'Classification: INFANT ATHLETE')
elif age <= 19:
    print(f'Classification: JUNIOR ATHLETE')
elif age <= 25:
    print(f'Classification: SENIOR ATHLETE')
else:
    print(f'Classification: MASTER ATHLETE')
    
