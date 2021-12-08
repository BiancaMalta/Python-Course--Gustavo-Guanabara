#Python Exercise 18

#Make a program that reads any angle and displays the sine, cosine and tangent value of that angle on the screen.
from math import radians, sin, cos, tan
ang = float(input('Enter the angle value: '))
print(f'The sine is {(sin(radians(ang))):.2f}\n'
      f'The cosine is {(cos(radians(ang))):.2f}\n'
      f'And the tangent is {(tan(radians(ang))):.2f}')
