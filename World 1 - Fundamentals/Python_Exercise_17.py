#Python Exercise 17

#Make a program that reads the length of the opposite side and the adjacent side of a right triangle, 
#calculates and displays the length of the hypotenuse.
from math import hypot
oside = float(input('Enter the length of the opposite side:\n'))
aside = float(input('Enter the length of the adjacent side:\n'))
print(f'The hypotenuse is {(hypot(oside, aside)):.2f}')
