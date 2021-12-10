#Python Exercise 58

#Make the computer "think" a number between 0 and 10,
#the player tries to guess until he gets it right, showing at the end how many guesses it took to win.
from random import randint

print('I will think in a number between 0 and 10. Try to guess.')
n = int(input('What number I thought? '))
r = randint(0, 10)
tries = 1
if n != r:
    print(f'You wrong!', end=" ")
    while n != r:
        if n > r:
            n = int(input('Try a smaller number: '))
            tries += 1
        else:
            n = int(input('Try a bigger number: '))
            tries += 1
print(f'''You won!
You guessed my number with {tries} tries!
It was nice playing with you!'')
