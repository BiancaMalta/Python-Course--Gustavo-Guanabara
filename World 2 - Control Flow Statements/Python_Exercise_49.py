#Python Exercise 49

#Make a multiplication table using a For loop.
print('MULTIPLICATION TABLE')
n = int(input('Enter a number: '))
for c in range (0, 11):
    print(f'{n} X {c} = {n * c}')
