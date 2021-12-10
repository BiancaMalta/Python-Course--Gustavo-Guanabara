#Python Exercise 62

#Improve the previous exercise by asking the user if he want to show some more terms.
n1 = int(input('Enter a number: '))
reason = int(input('Reason: '))
final_number = 1
nf = n1 + (10 - 1) * reason

while final_number != 0:
    while n1 != nf + reason:
        print(f'{n1}', end=" ")
        n1 += reason
    final_number = int(input('\nHow many more terms would you like to see? [enter 0 to exit]\n'))
    nf = n1 + (final_number - 1) * reason
