#Python Exercise 59

"""
Create a program that reads two values and displays a menu on the screen:
[1] Sum
[2] Multiply
[3] Better
[4] New numbers
[5] Quit
"""  
menu = 0
n1 = float(input('Enter the first number: '))
n2 = float(input('Enter the second number: '))
quit = False
while not quit:
    menu = int(input('''[1] Sum
[2] Multiply
[3] Better
[4] New Númbers
[5] Quit
 '''))
    if menu == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif menu == 2:
        print(f'{n1} X {n2} = {n1*n2}')
    elif menu == 3:
        if n1 != n2:
            list = sorted([n1, n2])
            print(f'The biggest number is {list[1]}')
        else:
            print(f'They are equal')
    elif menu == 4:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
    elif menu == 5:
        print(f'Exiting...')
        break
          
