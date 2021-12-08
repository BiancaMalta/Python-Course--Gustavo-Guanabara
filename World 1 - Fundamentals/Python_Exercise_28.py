#Python Exercise 28

#Write a program that makes the computer "think" of a whole number between 0 and 5 and ask the user to try 
#to figure it out. The program should write on the screen if the user won or lost.
from random import randint

print('I will think in a number between 0 and 5. Try to guess.')
n = int(input('What number I thought? '))
r = randint(0, 5)

if n == r:
    print('You won! You Guessed my number!')
else:
    print(f'You wrong! I thought in number {r} not {n}.')
   
