#Python Exercise 68

#Make a program that plays even or odd with the computer. 
#The game will only be stopped when the player LOSES, showing the total consecutive victories he has conquered at the end of the game.
from random import randint
n = c = 0
while True:
    choose = ''
    n = int(input('Enter a number: [1 to 10]\n'))
    pc = randint(1, 10)
    if 1 <= n <= 10:
        choose = input('Even or Odd? [E/O]\n').strip().upper()[0]
        if choose == 'E':
            if (pc + n) % 2 == 0:
                print(f'YOU WON!!! It is EVEN! You({n}) + ({pc})Computer = ({pc + n})')
                c += 1
            else:
                print(f'YOU LOST!!! It is ODD! You({n}) + ({pc})Computer = ({pc + n})')
                break
        elif choose == 'O':
            if (pc + n) % 2 == 1:
                print(f'YOU WON!!! It is ODD! You({n}) + ({pc})Computer = ({pc + n})')
                c += 1
            else:

                print(f'YOU LOST!!! It is EVEN! You({n}) + ({pc})Computer = ({pc + n})')
                break
        else:
            print('[ERROR] Only even or odd.')
    else:
        print('[ERROR] Only numbers from 1 to 10.')
print(f'You won {c} times!')
