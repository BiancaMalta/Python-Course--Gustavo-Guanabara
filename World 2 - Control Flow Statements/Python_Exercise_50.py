#Python Exercise 50

#Develop a program that reads six whole numbers and shows the sum of only those that are even.
print('Enter six Integers:')
sum = 0
for c in range(1, 7):
    n = int(input(f'number{c}: '))
    if n % 2 == 0:
        sum += n
print(f'The sum of even numbers is {sum}.')
