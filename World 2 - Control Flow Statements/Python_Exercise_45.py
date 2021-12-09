#Python Exercise 45

#Create a program that makes the computer play Jokenpô with you:
from random import randint

my_dict = {0: 'rock', 1: 'paper', 2: 'scissors'}
n = randint(0, 2)
m = int(input('''Let's play JOKENPO.Choose your play: 
[0] rock
[1] paper
[2] scissors
'''))
if m == n:
    print('DRAW GAME')
elif m == 0:
    if n == 1:
        print(f'You LOST! The computer chose {my_dict[n]}.')
    elif n == 2:
        print(f'You WON! The computer chose {my_dict[n]}.')
elif m == 1:
    if n == 0:
        print(f'You WON! The computer chose {my_dict[n]}.')
    elif n == 2:
        print(f'You LOST! The computer chose {my_dict[n]}.')
else:
    if n == 0:
        print(f'You LOST! The computer chose {my_dict[n]}.')
    elif n == 1:
        print(f'You WON! The computer chose {my_dict[n]}.')
