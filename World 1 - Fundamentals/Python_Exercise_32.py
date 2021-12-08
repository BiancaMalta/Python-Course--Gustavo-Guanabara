#Python Exercise 32

#Make a program that reads any year and shows you if it's LEAP.
from datetime import date

year = int(input('What Year? [Enter 0 to current year]: '))
if year == 0:
    year = date.today().year
if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    print(f'{year} is LEAP year')
else:
    print(f'{year} is NOT a leap year')
