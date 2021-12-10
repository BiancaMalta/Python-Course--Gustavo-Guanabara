#Python Exercise 60

#Make a program that reads any number and displays its factorial.
n = int(input('Enter the number to calculate its factorial: '))
counter = n
factorial = 1
while counter > 0:
    print(f'{counter}', end=' ')
    print(' X ' if counter>1 else ' = ', end=' ')
    factorial*=counter
    counter-=1
print(f'{factorial}')
