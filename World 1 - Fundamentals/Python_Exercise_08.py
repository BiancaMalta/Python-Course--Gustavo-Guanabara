#Python Exercise 08

#Make a program that reads a value in meters and displays it converted to kilometers, hectometers, decameters, decimeters, centimeters and millimeters.

m = float(input(f'Enter a distance in meters: '))

print(f'This distance in kilometers: {m / 1000}km \n'
      f'In hectometers: {m / 100}hm \n'
      f'In decameters: {m / 10}dam \n'
      f'In decimeters: {m * 10}dm \n'
      f'In centimeters: {m * 100}cm \n'
      f'And in millimeters: {m * 1000}mm')
