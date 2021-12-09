#Python Exercise 20

#Make a program that reads the names of the four students and shows the sequence drawn.
from random import shuffle
student1 = input('Student 1: ')
student2 = input('Student 2: ')
student3 = input('Student 3: ')
student4 = input('Student 4: ')
slist = [student1, student2, student3, student4]
shuffle(slist)
print(f'The sequence drawn is: {slist}')
