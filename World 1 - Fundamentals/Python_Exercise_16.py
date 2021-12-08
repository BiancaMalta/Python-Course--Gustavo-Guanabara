#Python Exercise 16

#Create a program that reads a real number and displays its entire number on the screen.
from math import trunc
n = float(input('Enter a number: '))
print(f'The number typed was {n} and its integer part is {trunc(n)}')
