#Python Exercise

#Create a program that reads the birth year of seven people and shows people who are not yet of age and are older.
from datetime import date
year = date.today().year
major = 0
minor = 0
for c in range(0,7):
    birth = int(input('What your birth year? '))
    age = year - birth
    if age >= 21:
        major += 1
    else:
        minor += 1
print(f'There are {major} adults and {minor} minors.')
