#Python Exercise 11

#Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, 
#knowing that each liter of paint paints an area of 2m².
print('Let\'s calculate how many liters of ink do you will need to paint a wall.')
w = float(input('Please, enter the wall\'s Width in meters: '))
h = float(input('Now enter the Height of the wall, in meters: '))
a = w * h
print(f'You needs {(a / 2):.1f} liters of ink to paint it.')
