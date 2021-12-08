#Python Exercise 19

#A teacher wants to draw one of his students to erase the board.
#Make a program that helps him by reading their name and writing the name of the chosen one.
from random import choice
student1 = input('First student: ')
student2 = input('Second student: ')
student3 = input('Third student: ')
student4 = input('Fourth student: ')
students = [student1, student2, student3, student4]
print(f'The chosen student is: {choice(students)}')
