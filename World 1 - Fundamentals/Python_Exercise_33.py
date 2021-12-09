#Python Exercise 33

#Make a program that reads three values and shows which is the biggest and which is the smallest.
print('Enter three integers:')
n1 = input('number1 > ').strip()
n2 = input('number2 > ').strip()
n3 = input('number3 > ').strip()

if n1 > n2 and n1 > n3:
    print(f'The biggest is {n1}')
elif n2 > n1 and n2 > n3:
    print(f'The biggest is {n2}')
elif n3 > n1 and n3 > n2:
    print(f'The biggest is {n3}')

if n1 < n2 and n1 < n3:
    print(f'The smallest is {n1}')
elif n2 < n1 and n2 < n3:
    print(f'The smallest is {n2}')
elif n3 < n1 and n3 < n2:
    print(f'The smallest is {n3}')
