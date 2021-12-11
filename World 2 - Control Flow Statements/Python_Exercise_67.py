#Python Exercise 67

#Make a program that displays the multiplication table of several numbers, one at a time, for each number entered by the user.
#The program will be stopped when the requested number is negative.
print('MULTIPLICATION TABLE')
n = cont = 0
while True:
    n = int(input('Enter a number:[number is negative to exit] '))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    cont = 0
print('END.')
